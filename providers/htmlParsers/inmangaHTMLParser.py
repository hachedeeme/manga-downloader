import re
from html.parser import HTMLParser

class InmangaHTMLParser(HTMLParser):
  def __init__(self):
    super(InmangaHTMLParser, self).__init__(convert_charrefs=True)
    self.data  = {}
    self.pageCounter = 1;

  def handle_starttag(self, tag, attrs):
    if tag == 'img':
      if ('class', 'ImageContainer') in attrs:
        for name, value in attrs:
          if name == 'id':
            self.data[self.pageCounter] = str(value)
            self.pageCounter += 1

  def reset_data(self):
    self.data = {}
    self.pageCounter = 1;