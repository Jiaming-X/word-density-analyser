from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from htmlPage import htmlPage
from ngram_processor import ngram_processor
import urllib2
import sys
import operator


# example commands:
# python main.py "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"

# python main.py "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"

# python main.py "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"


def main(argv):
    if not len(argv) == 2:
        print "Please enter url"
        return

    try:
        relevant_scores = {}

        aHtmlPage = htmlPage(argv[1]);
        results = ngram_processor(text = aHtmlPage.body, weight = 0.2, num = 4);
        relevant_scores = combine_dicts(relevant_scores, results.ngram_dict)

        results = ngram_processor(text = aHtmlPage.metaData, weight = 5.0, num = 4);
        relevant_scores = combine_dicts(relevant_scores, results.ngram_dict)

        results = ngram_processor(text = aHtmlPage.title, weight = 10.0, num = 4);
        relevant_scores = combine_dicts(relevant_scores, results.ngram_dict)

        print_top_n_elements(relevant_scores, 5)
    except:
        print "Unexpected error:", sys.exc_info()[0]
    pass

def combine_dicts(a, b, op=operator.add):
    return dict(a.items() + b.items() + [(k, op(a[k], b[k])) for k in set(b) & set(a)])

def print_top_n_elements(A, n):
    top_elements = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True)[:n])

    print "Scores | topics"
    for key, value in sorted(top_elements.items(), key=operator.itemgetter(1), reverse=True):
        print value, " | ", key
    pass

if __name__ == "__main__":
    main(sys.argv)


