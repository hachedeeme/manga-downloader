#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib.request
import urllib.parse

# import urllib.request
# url = 'https://httpbin.org/user-agent'
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
# request = urllib.request.Request(url,headers={'User-Agent': user_agent})
# response = urllib.request.urlopen(request)
# html = response.read()
# print(html)

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

  def test_server_connection(self, imageUrl):
    self.download_image(imageUrl, 'success.jpg')

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

  def upload_and_donwload_last(self):
    self.upload()
    self.download_last_manga()

  def download_mangas(self):
    self.provider.download(self)

  def upload(self):
    self.provider.upload_data(self)

  def download_last_manga(self):
    self.provider.download_last_manga(self)

  def download_last(self, amount):
    self.upload()
    self.provider.download_last(self, amount)

  def enumerate_exceptions(self):
    self.provider.enumerate_exceptions(self)

# downloader = MangaDownloader(1)
# downloader.test_server_connection('https://img1.tumangaonline.me/uploads/5af30e329b6b7/Ookii-Onnanoko-wa-Daisuki-Desu-ka-Ch.1-005.jpg')