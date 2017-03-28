from collections import Counter


def generate_ngrams(n, words):
    return [' '.join(words[i:i+n]) for i in xrange(len(words) - n+1)]


def ngram_statistics(n, words):
    ngrams = generate_ngrams(n, words)
    return Counter(ngrams)
