import codecs
from ranking import *

CORPUS_FILENAME = './data/potop.txt'


def clean_corpus(corpus):
    corpus = corpus.strip().lower()
    corpus = remove_special_characters(corpus)
    return corpus.split()


def read_corpus():
    with codecs.open(CORPUS_FILENAME, encoding='utf-8') as corpus_file:
        return clean_corpus(corpus_file.read())


if __name__ == '__main__':
    words = read_corpus()
    ranking = ranking(words)
    for rank, (word, occurences) in enumerate(ranking, start=1):
        print '{}. {}: {}'.format(rank, word.encode('utf-8'), occurences)
