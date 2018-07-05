import json

class Provider():

  def download(self, downloader):
    for chapter in self.chapters:
      self.download_chapter(downloader, chapter)

  def download_last_manga(self, downloader):
    self.download_chapter(downloader, self.data['last_chapter'])

  def download_last(self, downloader, amount):
    lastManga = self.data['last_chapter'] + 1
    firsManga = lastManga - amount
    # ========================================================================
    print("Downloading from %s to %s." % (firsManga, lastManga - 1))
    # ========================================================================
    for chapter in range(firsManga, lastManga):
      self.download_chapter(downloader, chapter)

  def download_chapter(self, downloader, chapter):
    pass
  
  def upload_data(self, downloader):
    htmlSource = downloader.get_html(self.data['source_url'])
    self.updater.upload(htmlSource)

  def set_chapters(self, chapters):
    self.chapters = chapters

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

  def get_dir_name(self, chapter):
    return self.mangaName + '/' + self.mangaName + ' ' +  self.get_chapter_name(chapter)