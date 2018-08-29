import httpUtils
import re

from providers.htmlParsers.ninemangaHTMLParser   import NinemangaHTMLParser
from providers.updaters.ninemangaChaptersUpdater import NinemangaChaptersUpdater

from providers.provider import Provider

class Ninemanga(Provider):
  def __init__(self, mangaId, chapters=[]):
    dataFileUrl = 'providers/data/ninemanga/' + mangaId + '.json'
    # ============================================================================================
    self.data   = self.load_data(dataFileUrl)
    self.parser = NinemangaHTMLParser()
    self.chapters  = chapters
    self.mangaName = self.data['name']
    self.updater   = NinemangaChaptersUpdater(dataFileUrl, self.data)
    self.url       = 'http://es.ninemanga.com'

  def download_chapter(self, downloader, chapter):
    chapterUrl= self.data['chapters'][str(chapter)]
    downloader.parse_html(chapterUrl)
    allPages = self.parser.data['pages']
    dirName  = self.mangaName + '/' + self.mangaName + ' ' +  self.get_chapter_name(chapter)
    downloader.make_directory(dirName)
    for page in sorted(allPages):
      downloader.parse_html(self.url + allPages[page])
      imageName = self.mangaName + ' ' +  self.get_chapter_name(chapter) + '-' + ('0' + str(page) if page < 10 else str(page)) + '.jpg'
      print('Image Url: ' + self.parser.data['imageUrl'])
      downloader.download_image(httpUtils.iri2uri(self.parser.data['imageUrl']), dirName + '/' + imageName)
      print('Generate: ' + dirName + '/' + imageName)
      print('================================================================================================')

    self.parser.reset_data() # Reset de data for next chapter