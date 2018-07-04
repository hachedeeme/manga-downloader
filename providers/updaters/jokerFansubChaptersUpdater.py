import re
from html.parser import HTMLParser

from providers.updaters.providerChaptersUpdater import ProviderChaptersUpdater

class JokerFansubChaptersUpdater(ProviderChaptersUpdater):
  def __init__(self, destinyFileUrl, data):
    ProviderChaptersUpdater.__init__(self, destinyFileUrl, data)
    self.providerName = 'JokerFansub'
    self.providerURL  = 'https://jokerfansub.com'

  def upload_missing_chapters(self, missingChapters):
    uploadList = []
    for chapterNumber, url, title in missingChapters:
      self.data['chapters'][str(chapterNumber)] = { "url": url, "title": title }
      self.data['last_chapter'] = int(chapterNumber)
      uploadList.append(chapterNumber)
    return uploadList

  def find_chapters(self, source):
    parse_data = lambda data: (self.get_chapter_number(data[0]), data[0], self.get_title(data[1]))
    res = re.findall('<div class="title"><a href="(.*)" title="(.*)">(.*)</a></div>', source)
    return list(map(parse_data, res))

  def get_title(self, title):
    return title.split(': ')[1]

  def get_chapter_number(self, url):
    return int(url.split('/')[-2])