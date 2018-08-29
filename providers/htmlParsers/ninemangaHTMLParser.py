import re
from html.parser import HTMLParser

class NinemangaHTMLParser(HTMLParser):
  def __init__(self):
    super(NinemangaHTMLParser, self).__init__(convert_charrefs=True)
    self.data = { "pages": { } }
    self.pageCounter = 1;

  def handle_starttag(self, tag, attrs):
    if tag == 'img':
      if ('id', 'manga_pic_1') in attrs:
        for name, value in attrs:
          if name == 'src':
            self.data['imageUrl'] = str(value)
    if tag == 'a':
      if ('style', 'float:none;') in attrs:
        for name, value in attrs:
          if name == 'href':
            self.data['pages'][self.pageCounter] = str(value)
            self.pageCounter += 1

  def reset_data(self):
    self.data = { "pages": { } }
    self.pageCounter = 1;