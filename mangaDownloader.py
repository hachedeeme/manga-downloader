#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib.request
import urllib.parse

class MangaDownloader():
  def __init__(self, provider):
    self.provider = provider
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
    self.provider.feed(html)

  def download_mangas(self):
    self.provider.download(self)

  def upload(self):
    self.provider.upload_data(self)