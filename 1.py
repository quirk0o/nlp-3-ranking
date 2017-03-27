import codecs
from ranking import *
from preprocessor import *

CORPUS_FILENAME = './data/potop.txt'


def read_corpus():
    with codecs.open(CORPUS_FILENAME, encoding='utf-8') as corpus_file:
        return clean_corpus(corpus_file.read())


if __name__ == '__main__':
    words = read_corpus()
    ranking, most_common = ranking(words)
    for rank, (word, frequency) in enumerate(most_common, start=1):
        print '{}. {}: {}'.format(rank, word.encode('utf-8'), frequency)
