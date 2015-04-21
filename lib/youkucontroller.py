import urllib2
from HTMLParser import HTMLParser
class LibHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.flag=0
        self.i=0
        self.dic = {}
 
    def handle_starttag(self, tag, attrs):
        if tag == "div" and len(attrs)>=1:
            if len(attrs)==2 and attrs[1][0]=='c_time' and self.flag==0:
                self.flag = 1
                self.dic['time']=attrs[1][1]
            if attrs[0][0]=='class' and attrs[0][1]=='v-link':
                self.flag = 2
        if tag == "a" and self.flag == 2:
            self.flag = 0
            self.dic['title']=attrs[0][1]
            self.dic['link']=attrs[2][1]
            if self.dic.has_key("time") and self.dic.has_key("title") and self.dic.has_key("link"):
                self.links.append(self.dic)
            self.dic = {}

def get_video_from_lib(url):
    html_code = urllib2.urlopen(url).read()
    hp = LibHTMLParser()
    hp.feed(html_code)
    hp.close()
    return hp.links
