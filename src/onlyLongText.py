from bs4 import SoupStrainer
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

only_a_tags = SoupStrainer("a")

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(text):
    #return True
    return len(text) > 30

only_short_strings = SoupStrainer(text = is_short_string)

#print(BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags).prettify())

#print(BeautifulSoup(html_doc, "html.parser", parse_only=only_tags_with_id_link2).prettify())

#print(BeautifulSoup(html_doc, "lxml").prettify())

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())





html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
;and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""
