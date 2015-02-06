#!/usr/bin/env python
import collections
s='AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
d = collections.defaultdict(list)
h,t = 0,9
end =len(s)
while t <= end:
    d[hash(s[h:t+1])].append(s[h:t+1])
    h+=1
    t+=1
print [seq[0] for seq in d.values()  if len(seq) > 1 ]
