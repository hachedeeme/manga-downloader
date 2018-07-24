import httpUtils

# from providers.htmlParsers.jokerFansubHTMLParser   import JokerFansubHTMLParser
from providers.updaters.kissmangaChaptersUpdater   import KissmangaChaptersUpdater

from providers.provider import Provider

class Kissmanga(Provider):
  def __init__(self, mangaId, chapters=[]):
    dataFileUrl = 'providers/data/kissmanga/' + mangaId + '.json'
    # ============================================================================================
    self.data   = self.load_data(dataFileUrl)
    self.parser = None
    self.chapters  = chapters
    self.mangaName = self.data['name']
    self.updater   = KissmangaChaptersUpdater(dataFileUrl, self.data)

  def download_chapter(self, downloader, chapter):
    pass
    # currentChapter = self.data['chapters'][str(chapter)]
    # downloader.parse_html(currentChapter['url'] + 'page/1')

    # dirName  = self.get_dir_name(chapter) + ' - ' + currentChapter['title']
    # downloader.make_directory(dirName)
    # lastPage = self.parser.data['lastPage'] + 1

    # for page in range(1, lastPage):
    #   downloader.parse_html(currentChapter['url'] + 'page/' + str(page))
    #   imageName = self.mangaName + ' ' +  self.get_chapter_name(chapter) + '-' + ('0' + str(page) if page < 10 else str(page)) + '.jpg'

    #   print('Image Url: ' + self.parser.data['imagePath'])
    #   downloader.download_image(httpUtils.iri2uri(self.parser.data['imagePath']), dirName + '/' + imageName)
    #   print('Generate: ' + dirName + '/' + imageName)