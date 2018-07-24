import re
from html.parser import HTMLParser

from providers.updaters.providerChaptersUpdater import ProviderChaptersUpdater

class KissmangaChaptersUpdater(ProviderChaptersUpdater):
  def __init__(self, destinyFileUrl, data):
    ProviderChaptersUpdater.__init__(self, destinyFileUrl, data)
    self.providerName = 'Kissmanga'
    self.providerURL  = 'https://kissmanga.com'

  def upload_missing_chapters(self, missingChapters):
    uploadList = []
    for chapterNumber, url in missingChapters:
      self.data['chapters'][str(chapterNumber)] = { "url": url }
      self.data['last_chapter'] = chapterNumber
      uploadList.append(chapterNumber)
    return uploadList

  def find_chapters(self, source):
    parse_data = lambda data: (self.get_chapter_number(data[1]), data[0])
    res = re.findall('<td>\n<a href="(.*)" title="(.*)">\n(.*)</a>\n</td>', source)
    return list(map(parse_data, res))

  def get_chapter_number(self, url):
    return int(url.split(' ')[-2])