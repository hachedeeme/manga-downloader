import json

class Provider():

  def feed(self, html):
    self.parser.feed(html)

  def get_file_name(self, vol, chapter, page):
    return 'Vol' + self.get_vol_name(vol) + '-Ch' + self.get_chapter_name(chapter) + '-' + ('0' + str(page) if page < 10 else str(page)) + '.jpg'

  def get_vol_name(self, volNumber):
    if volNumber < 10:
      return '00' + str(volNumber)
    elif volNumber < 100:
      return '0' + str(volNumber)
    else:
      return str(volNumber)

  def get_chapter_name(self, chapterNumber):
    if chapterNumber < 10:
      return '000' + str(chapterNumber)
    elif chapterNumber < 100:
      return '00' + str(chapterNumber)
    elif chapterNumber < 1000:
      return '0' + str(chapterNumber)
    else:
      return str(chapterNumber)

  def load_data(self, jsonPath):
    res = {}
    with open(jsonPath) as data:
      res = json.load(data)
    return res
