import codecs
from preprocessor import *
from ngrams import ngram_statistics

CORPUS_FILENAME = './data/potop.txt'


def read_corpus():
    with codecs.open(CORPUS_FILENAME, encoding='utf-8') as corpus_file:
        return clean_corpus(corpus_file.read())


if __name__ == '__main__':
    words = read_corpus()
    digrams = ngram_statistics(2, words)
    trigrams = ngram_statistics(3, words)

    print "\nDigrams"
    for digram, count in digrams.most_common(100):
        print '{}: {}'.format(digram.encode('utf-8'), count)

    print '----------'
    print "\nTrigrams"
    for trigram, count in trigrams.most_common(100):
        print '{}: {}'.format(trigram.encode('utf-8'), count)
