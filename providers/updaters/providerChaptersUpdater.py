import json

class ProviderChaptersUpdater():
  def __init__(self, destinyFileUrl, data):
    self.fileURL = destinyFileUrl
    self.data    = data
    self.mangaName    = self.data['name']
    self.lastChapter  = self.data['last_chapter']

  def upload(self, source):
    missingData = self.get_upload(source, self.data['last_chapter'])
    if not missingData:
      print("Data of %s manga on %s provider is Already Updated. Current chapter in '%s' is: %s." % (self.mangaName, self.providerName, self.providerURL, self.lastChapter))
    else:
      # ====================================================
      uploadList = self.upload_missing_chapters(missingData)
      # ====================================================
      with open(self.fileURL, 'w') as data_json:
        json.dump(self.data, data_json, sort_keys=True)
        print(self.chapters_updated_msg(self.data['name'], uploadList))

  def upload_missing_chapters(self, missingChapters):
    pass

  def get_upload(self, source, currentManga):
    allChapters = self.find_chapters(source)
    allChapters.sort()
    return list(filter(lambda current: int(current[0]) > currentManga, allChapters))

  def chapters_updated_msg(self, name, chapters):
    msg = 'chapter'
    if len(chapters) == 1:
      msg += ' %s' % chapters[0]
    elif len(chapters) == 2:
      msg += 's %s and %s' % (chapters[0], chapters[1])
    else:
      msg += 's %s at %s' % (chapters[0], chapters[-1])
    return 'Updated %s of %s manga.' % (msg, name)

  # =============================================================================
  # ACCESSORS
  # =============================================================================
  def get_numbers_on_title(self):
    return self.data['numbers_on_title'] if 'numbers_on_title' in self.data else []