import codecs

import matplotlib.pyplot as plt
from plot import plot_stats

RANKING_FILENAME = './out/ranking.dat'

if __name__ == '__main__':
    with codecs.open(RANKING_FILENAME, encoding='utf-8') as ranking_file:
        lines = ranking_file.read().strip().split('\n')
        ranking = [line.split(':') for line in lines]
        ranking = [(rank[0], int(rank[1])) for rank in ranking]
        plot_stats(ranking)
        plt.show()
