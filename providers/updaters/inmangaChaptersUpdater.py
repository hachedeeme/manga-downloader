import re
from html.parser import HTMLParser

from providers.updaters.providerChaptersUpdater import ProviderChaptersUpdater

class InmangaChaptersUpdater(ProviderChaptersUpdater):
  def __init__(self, destinyFileUrl, data):
    ProviderChaptersUpdater.__init__(self, destinyFileUrl, data)
    self.providerName = 'Inmanga'
    self.providerURL  = 'https://inmanga.com'

  def upload_missing_chapters(self, missingChapters):
    uploadList = []
    for chapterNumber, chapterId in missingChapters:
      self.data['chapters'][chapterNumber] = chapterId
      self.data['last_chapter'] = int(chapterNumber)
      uploadList.append(chapterNumber)
    return uploadList

  def find_chapters(self, source):
    fistIndex = re.search('<select class="form-control ChapterListClass" id="ChapList"', source).span(0)[0]
    lastIndex = re.search('</select>', source).span(0)[1]
    htmlSelect = source[fistIndex:lastIndex].replace('selected="selected" ','')
    return list(map(lambda current: (current[1], current[0]), re.findall('<option value="(.*)">(.*)</option>', htmlSelect)))