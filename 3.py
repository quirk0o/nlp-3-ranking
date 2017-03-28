import codecs
from stats import *

RANKING_FILENAME = './out/ranking.dat'

if __name__ == '__main__':
    with codecs.open(RANKING_FILENAME, encoding='utf-8') as ranking_file:
        lines = ranking_file.read().strip().split('\n')
        ranking = [line.split(':') for line in lines]
        ranking = [(rank[0], int(rank[1])) for rank in ranking]

        hapax_legomena = hapax_legomena(ranking)
        half_of_text = half_of_text(ranking)
        print 'Hapax legomena: {}'.format(len(hapax_legomena))
        print '50% of corpus: {}'.format(len(half_of_text))
