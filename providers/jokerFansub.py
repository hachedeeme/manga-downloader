import httpUtils

from providers.htmlParsers.jokerFansubHTMLParser import JokerFansubHTMLParser
from providers.provider import Provider

class JokerFansub(Provider):
  def __init__(self, mangas, url, path):
    self.parser = JokerFansubHTMLParser(url)
    self.mangas = mangas
    self.path   = path

  def download(self, downloader):
    for vol in self.mangas.keys():
      currentPath = self.path
      currentPath = currentPath.replace('VOL', str(vol))

      for chapter in self.mangas[vol]:
        path = currentPath
        path = path.replace('CHAPTER', str(chapter))

        # Try to get html from path
        downloader.parse_html(path + '1')
        
        dirName = 'Vol ' + self.get_vol_name(vol) + '/Capitulo ' +  self.get_chapter_name(chapter) + ' - ' + self.parser.find_chapter_name(vol, chapter)
        
        downloader.make_directory(dirName)
        lastPage = self.parser.data['lastPage'] + 1

        for page in range(1, lastPage):
          downloader.parse_html(path + str(page))

          imageName = self.get_file_name(vol, chapter, page)
          print(self.parser.data['imagePath'])
          downloader.download_image(httpUtils.iri2uri(self.parser.data['imagePath']), dirName + '/' + imageName)
          print('generate ' + dirName + '/' + imageName)

  def feed(self, html):
    self.parser.feed(html)