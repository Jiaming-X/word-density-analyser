import operator


class ngram_processor:
    body = ""
    words = ""
    replace_symbols = ["...", ".", ",", "? ", ": ", '"', '|', "'", "--"]
    stop_words = []
    ngram_dict = {}
    n = 2

    def __init__(self, text, weight, num=2):
        self.n = num
        text = text.lower()
        self.body = text
        #self.words = text.split();
        self.words = self.tokenize(text)
        self.load_stop_words()
        self.construct_ngram(weight)
        pass

    def tokenize(self, text):

        for symbol in self.replace_symbols:
            text = text.replace(symbol, " ")
        return text.split()

    def load_stop_words(self):
        with open('stop_words.txt', 'r') as f:
            self.stop_words = f.read().splitlines()

    def construct_ngram(self, weight):
        meaning_words = []

        for word in self.words:
            if (not (word in self.stop_words)) and len(word) > 3:
                meaning_words.append(word)

        for j in range(2, self.n + 1):
            for i in range(len(meaning_words) - j + 1):
                key = ""
                for k in range(i, i + j):
                    key += (meaning_words[k] + " ")
                key = key.strip()
                if self.ngram_dict.has_key(key):
                    self.ngram_dict[key] += weight
                else:
                    self.ngram_dict[key] = weight

        self.ngram_dict = dict(sorted(self.ngram_dict.items(), key=operator.itemgetter(1), reverse=True))
        pass
