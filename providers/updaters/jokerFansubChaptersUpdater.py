import re
import json
from html.parser import HTMLParser

class JokerFansubChaptersUpdater():
  def __init__(self, destinyFileUrl, data):
    self.file_url = destinyFileUrl
    self.data     = data

  def upload(self, source):
    missingData = self.get_upload(source, self.data['last_chapter'])
    if not missingData:
      print("Data of %s manga on JokerFansub provider is Already Updated. Current chapter in 'https://jokerfansub.com' is: %s." % (self.data['name'], self.data['last_chapter']))
    else:
      upload_list = []
      for chapterNumber, url, title in missingData:
        self.data['chapters'][str(chapterNumber)] = { "url": url, "title": title }
        self.data['last_chapter'] = int(chapterNumber)
        upload_list.append(chapterNumber)
      
      with open(self.file_url, 'w') as data_json:
        json.dump(self.data, data_json, sort_keys=True)
        print('Updated chapters %s of %s manga.' % (upload_list, self.data['name']))

  # def chapters_updated_msg(self, chapters):
  #   pass

  def get_upload(self, source, currentManga):
    allChapters = self.find_chapters(source)
    allChapters.sort()
    return list(filter(lambda current: int(current[0]) > currentManga, allChapters))

  def find_chapters(self, source):
    parse_data = lambda data: (self.get_chapter_number(data[0]), data[0], self.get_title(data[1]))
    res = re.findall('<div class="title"><a href="(.*)" title="(.*)">(.*)</a></div>', source)
    return list(map(parse_data, res))

  def get_title(self, title):
    return title.split(': ')[1]

  def get_chapter_number(self, url):
    return int(url.split('/')[-2])