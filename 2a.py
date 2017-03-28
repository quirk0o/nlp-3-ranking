import codecs
from ranking import *
from preprocessor import *

CORPUS_FILENAME = './data/potop.txt'
OUTPUT_FILENAME = './out/ranking.dat'


def read_corpus():
    with codecs.open(CORPUS_FILENAME, encoding='utf-8') as corpus_file:
        return clean_corpus(corpus_file.read())


if __name__ == '__main__':
    words = read_corpus()
    ranking, most_common = ranking(words)
    with codecs.open(OUTPUT_FILENAME, encoding='utf-8', mode='w') as output_file:
        for word, frequency in ranking:
            output_file.write(word)
            output_file.write(':')
            output_file.write(str(frequency))
            output_file.write('\n')
