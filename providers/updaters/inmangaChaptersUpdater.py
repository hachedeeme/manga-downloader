import re
import json
from html.parser import HTMLParser

class InmangaChaptersUpdater():
  def __init__(self, destinyFileUrl, data):
    self.file_url = destinyFileUrl
    self.data     = data

  def upload(self, source):
    missingData = self.get_upload(source, self.data['last_chapter'])
    if not missingData:
      print("Data of %s manga on Inmanga provider is Already Updated. Current chapter in 'https://inmanga.com' is: %s." % (self.data['name'], self.data['last_chapter']))
    else:
      upload_list = []
      for chapterId, chapterNumber in missingData:
        self.data['chapters'][chapterNumber] = chapterId
        self.data['last_chapter'] = int(chapterNumber)
        upload_list.append(chapterNumber)
      
      with open(self.file_url, 'w') as data_json:
        json.dump(self.data, data_json, sort_keys=True)
        print('Updated chapters %s of %s manga.' % (upload_list, self.data['name']))

  def get_upload(self, source, currentManga):
    allChapters = self.find_chapters(source)
    return list(filter(lambda current: int(current[1]) > currentManga, allChapters))

  def find_chapters(self, source):
    fistIndex = re.search('<select class="form-control ChapterListClass" id="ChapList"', source).span(0)[0]
    lastIndex = re.search('</select>', source).span(0)[1]
    htmlSelect = source[fistIndex:lastIndex].replace('selected="selected" ','')
    return re.findall('<option value="(.*)">(.*)</option>', htmlSelect)