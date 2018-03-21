#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib.request
import urllib.parse
import httpUtils

class MangaDownloader():
  def __init__(self, mangas, path, parser):
    self.mangas = mangas
    self.path   = path
    self.parser = parser
    # Essential data
    self.data    = urllib.parse.urlencode({}).encode('ascii')
    self.headers = { 'User-Agent' : 'whatever' }

  def get_html(self, currentPath):
    html = ""
    try:
      request = urllib.request.Request(currentPath, self.data, self.headers)
      html    = urllib.request.urlopen(request).read().decode('utf8')
    except urllib.error.HTTPError as error:
      print(str(error))
    except urllib.error.URLError as error:
      print(str(error) + ' - Invalid URL or have not internet conection')
    except Exception as e:
      print('ERROR GROSO: Se econtró un error de esta clase: ' + str(type(e)))
    finally:
      return html

  def download_image(self, imagePath, imageName):
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'whatever')
    filename, headers = opener.retrieve(imagePath, imageName)

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

  def make_directory(self, dirName):
    os.makedirs(dirName)

  def parse_html(self, path):
    timelimit = 1
    ok = False
    html = ""
    while not ok and timelimit < 10:
      print('try get first time from: ' + path)
      html = self.get_html(path)
      if not (html == ""):
        print("It's okey")
        ok = True
      else:
        print('Try number ' + str(timelimit))
        timelimit += 1
    self.parser.feed(html)

  def download_mangas(self):
    for vol in self.mangas.keys():
      currentPath = self.path
      currentPath = currentPath.replace('VOL', str(vol))

      for chapter in self.mangas[vol]:
        path = currentPath
        path = path.replace('CHAPTER', str(chapter))

        # Try to get html from path
        self.parse_html(path + '1')
        
        dirName = 'Vol ' + self.get_vol_name(vol) + '/Capitulo ' +  self.get_chapter_name(chapter) + ' - ' + self.parser.find_chapter_name(vol, chapter)
        
        self.make_directory(dirName)
        lastPage = self.parser.data['lastPage'] + 1

        for page in range(1, lastPage):
          self.parse_html(path + str(page))

          imageName = self.get_file_name(vol, chapter, page)
          print(self.parser.data['imagePath'])
          self.download_image(httpUtils.iri2uri(self.parser.data['imagePath']), dirName + '/' + imageName)
          print('generate ' + dirName + '/' + imageName)