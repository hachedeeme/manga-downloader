import httpUtils

from providers.htmlParsers.inmangaHTMLParser   import InmangaHTMLParser
from providers.updaters.inmangaChaptersUpdater import InmangaChaptersUpdater

from providers.provider import Provider

class Inmanga(Provider):
  def __init__(self, mangaId, chapters=[]):
    self.parser = InmangaHTMLParser()
    self.chapterUrl = 'https://inmanga.com/Chapter?id='
    self.imageUrl   = 'https://inmanga.com/page/getPageImage/?identification='
    self.chapters   = chapters
    # ============================================================================================
    dataFileUrl = 'providers/data/inmanga/' + mangaId + '.json'
    # ============================================================================================
    self.data = self.load_data(dataFileUrl)
    self.updater   = InmangaChaptersUpdater(dataFileUrl, self.data)
    self.mangaName = self.data['name']

  def download_chapter(self, downloader, chapter):
    downloader.parse_html(self.chapterUrl + self.data['chapters'][str(chapter)])

    dirName = self.mangaName + '/' + self.mangaName + ' ' +  self.get_chapter_name(chapter)
    downloader.make_directory(dirName)

    for page in sorted(self.parser.data):
      imageName = self.mangaName + ' ' +  self.get_chapter_name(chapter) + '-' + ('0' + str(page) if page < 10 else str(page)) + '.jpg'
      print('Image Url: ' + self.imageUrl + self.parser.data[page])
      downloader.download_image(httpUtils.iri2uri(self.imageUrl + self.parser.data[page]), dirName + '/' + imageName)
      print('Generate: ' + dirName + '/' + imageName)

    self.parser.reset_data() # Reset de data for next chapter