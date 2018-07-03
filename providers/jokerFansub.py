import httpUtils

from providers.htmlParsers.jokerFansubHTMLParser   import JokerFansubHTMLParser

from providers.provider import Provider

class JokerFansub(Provider):
  def __init__(self, mangaId, chapters=[]):
    dataFileUrl = 'providers/data/jokerFansub/' + mangaId + '.json'
    # ============================================================================================
    self.data   = self.load_data(dataFileUrl)
    self.path   = self.data['source_url'] + '/VOL/CHAPTER/page/'
    self.parser = JokerFansubHTMLParser(self.data['source_url'] + '/')
    self.chapters  = chapters
    self.mangaName = self.data['name']

  def download_chapter(self, downloader, chapter):
    vol = self.data['chapters'][str(chapter)]
    currentPath = self.path
    currentPath = currentPath.replace('VOL', vol).replace('CHAPTER', str(chapter))

    # Try to get html from path
    downloader.parse_html(currentPath + '1')

    dirName  = self.get_dir_name(chapter) + ' - ' + self.parser.find_chapter_name(vol, chapter)
    downloader.make_directory(dirName)
    lastPage = self.parser.data['lastPage'] + 1

    for page in range(1, lastPage):
      downloader.parse_html(currentPath + str(page))
      imageName = self.mangaName + ' ' +  self.get_chapter_name(chapter) + '-' + ('0' + str(page) if page < 10 else str(page)) + '.jpg'

      print('Image Url: ' + self.parser.data['imagePath'])
      downloader.download_image(httpUtils.iri2uri(self.parser.data['imagePath']), dirName + '/' + imageName)
      print('Generate: ' + dirName + '/' + imageName)