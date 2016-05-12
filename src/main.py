from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from htmlPage import htmlPage
from ngram_processor import ngram_processor
import urllib2
import sys
import operator


# python main.py "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"

# python main.py "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"

# python main.py "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"


def main(argv):
    relevant_scores = {}

    aHtmlPage = htmlPage(argv[1]);
    results = ngram_processor(aHtmlPage.body, 0.2);
    relevant_scores = combine_dicts(relevant_scores, results.ngram_dict)

    results = ngram_processor(aHtmlPage.metaData, 5.0);
    relevant_scores = combine_dicts(relevant_scores, results.ngram_dict)
    #print aHtmlPage.metaData

    results = ngram_processor(aHtmlPage.title, 10.0);
    relevant_scores = combine_dicts(relevant_scores, results.ngram_dict)
    #print aHtmlPage.title

    relevant_scores = sorted(relevant_scores.items(), key=operator.itemgetter(1))

    print relevant_scores

    #print aHtmlPage.metaData
    #print results.words
    #for word in results.words:
    #    print word, " ",
    #print results.stop_words
    #for word in results.stop_words:
    #    print word, " ",
    pass

def combine_dicts(a, b, op=operator.add):
    return dict(a.items() + b.items() + [(k, op(a[k], b[k])) for k in set(b) & set(a)])

if __name__ == "__main__":
    main(sys.argv)


