#!/usr/bin/env python

from collections import defaultdict

twos = 0
threes = 0

for line in open('input'):
    c = defaultdict(int)
    map(lambda x: c.__setitem__(x, c[x]+1), line)
    twos += bool(len([k for k, v in c.items() if v == 2]))
    threes += bool(len([k for k, v in c.items() if v == 3]))
    #print repr(c), twos, threes
    #break

print twos, threes, twos*threes
