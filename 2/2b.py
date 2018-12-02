#!/usr/bin/env python

import sys


def checkpair(a, b):
    same = map(lambda x: x[0] != x[1], zip(a, b))

    if sum(same) == 1:
        return ''.join([x[0] for x in zip(a, b, same) if not x[2]])


words = open('input').read().splitlines()
for w1 in words:
    for w2 in words:
        foo = checkpair(w1, w2)
        if foo:
            print w1
            print w2
            print foo
            sys.exit(0)
