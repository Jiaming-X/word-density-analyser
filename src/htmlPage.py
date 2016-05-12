from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2
import re
import sys
import requests

class htmlPage:
    'Common base class for all html'
    html = ""
    html_formatted = ""
    title = ""
    metaData = ""
    body = ""

    def __init__(self, url):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36")]
        self.html = opener.open(url).read()
        #self.html = requests.get(url)#urllib2.urlopen(url).read()
        soup = BeautifulSoup(self.html, "lxml")

        #print type(str(self.html))
        #print html_doc

        self.html_formatted = soup.prettify()
        self.title = soup.title.string;

        desc = soup.findAll(attrs={"name":"description"})
        self.metaData = desc[0]['content'].encode('utf-8')

        #[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        #self.body = soup.getText(separator=u' ')
        #print desc['content'].encode('utf-8')

        parser = SoupStrainer(self.is_long_string)
        soup2 = BeautifulSoup(self.html, "html.parser", parse_only=parser)
        [s.extract() for s in soup2(['style', 'script', '[document]', 'head', 'title'])]
        self.body = soup2.getText(separator=u' ')
        #print soup2.get_text().encode('utf-8')

    def is_long_string(text, *arg):
        return len(str(text)) > 20
