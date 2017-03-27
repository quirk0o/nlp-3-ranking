# coding=utf-8
from collections import Counter

from plp import PLP

p = PLP()


def basic_form(word):
    ids = p.rec(word)
    return p.bform(ids[0]) if len(ids) > 0 else word


def ranking(words):
    basic_forms = [basic_form(word) for word in words]
    stats = Counter(basic_forms)
    return sorted(stats.items(), key=lambda x: x[1], reverse=True)
