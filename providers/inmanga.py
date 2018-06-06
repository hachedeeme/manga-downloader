import httpUtils

from providers.htmlParsers.inmangaHTMLParser import InmangaHTMLParser
from providers.provider import Provider

class Inmanga(Provider):
  def __init__(self, mangaId, chapters):
    self.parser = InmangaHTMLParser()
    self.chapterUrl = 'https://inmanga.com/Chapter?id='
    self.imageUrl   = 'https://inmanga.com/page/getPageImage/?identification='
    self.chapters   = chapters
    
    data = self.load_data('providers/data/inmanga/' + mangaId + '.json')
    self.data       = data['caps']
    self.mangaName  = data['name']

  def download(self, downloader):
    for chapter in self.chapters:
      downloader.parse_html(self.chapterUrl + self.data[str(chapter)])

      dirName = self.mangaName + '/' + self.mangaName + ' ' +  self.get_chapter_name(chapter)
      downloader.make_directory(dirName)

      for page in sorted(self.parser.data):
        imageName = self.mangaName + ' ' +  self.get_chapter_name(chapter) + '-' + ('0' + str(page) if page < 10 else str(page)) + '.jpg'
        print('Image Url: ' + self.imageUrl + self.parser.data[page])
        downloader.download_image(httpUtils.iri2uri(self.imageUrl + self.parser.data[page]), dirName + '/' + imageName)
        print('Generate: ' + dirName + '/' + imageName)

      self.parser.reset_data()