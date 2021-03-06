import re

from providers.updaters.providerChaptersUpdater import ProviderChaptersUpdater

class NinemangaChaptersUpdater(ProviderChaptersUpdater):
  def __init__(self, destinyFileUrl, data):
    ProviderChaptersUpdater.__init__(self, destinyFileUrl, data)
    self.providerName = 'Ninemanga'
    self.providerURL  = 'http://es.ninemanga.com/'

  def upload_missing_chapters(self, missingChapters):
    uploadList = []
    for chapterNumber, chapterKey, url in missingChapters:
      self.data['chapters'][chapterKey] = url
      self.data['last_chapter'] = chapterNumber
      uploadList.append(chapterNumber)
    return uploadList
    
  def find_chapters(self, source):
    chapter_data_by_key = lambda data, key: self.get_chapter_number_data(data[1])[key]
    parse_data = lambda data: (chapter_data_by_key(data, 'chapter_number'), chapter_data_by_key(data, 'key'), data[0])
    res = re.findall('<a class="chapter_list_a" href="(.*)" title="(.*)">(.*)</a>', source)
    return list(map(parse_data, res))

  def get_chapter_number_data(self, strSource):
    chapter_number = self.get_chapter_number(strSource)
    return { "key": str(chapter_number[0]), "chapter_number": int(chapter_number[0]) } if len(chapter_number) == 1 else self.get_exception(strSource)

  def get_exception(self, key):
    return self.data['exeptions'][key]

  def enumerate_exceptions(self, source):
    parse_data = lambda data: (data[1], self.get_chapter_number(data[1]))
    res = re.findall('<a class="chapter_list_a" href="(.*)" title="(.*)">(.*)</a>', source)
    filter_exceptions = lambda data: len(data[1]) != 1 # Cuando se encuentran más de un número de capítulo
    chapters = list(filter(filter_exceptions, map(parse_data, res)))
    # enumera las excepciones
    exeptions = {}
    for chapter in chapters:
      if chapter[1]:
        exeptions[chapter[0]] = { "chapter_number": int(chapter[1][0]), "key": ".".join(chapter[1]) }
      else:
        exeptions[chapter[0]] = { "chapter_number": 0, "key": chapter[0] }
    print(exeptions)

  def get_chapter_number(self, source):
    res = re.findall('\d+', source)
    for number in self.get_numbers_on_title():
      res.remove(number)
    return res