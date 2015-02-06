#!/usr/bin/env python

S='ADOBECODEBANC'
T='ABC'
if len(S) < len(T) or len(S) == 0 or len(T) == 0:
    print ""
    
if len(S) == 1:
    if S == T:
        print S
    else:
        print ""
    
alpha = { 'a': 3, 'b':5, 'c':7, 'd':11, 'e':13, 'f':17, 'g':19, 'h':23, 'i':29, 'j':31, 'k':37, 'l':41, 'm':43, 'n':47, 'o':53, 'p':59, 'q':61, 'r':67, 's':71, 't':73, 'u':79, 'v':83, 'w':89, 'x':97, 'y':101, 'z':103, '_':107}
d={}
end = len(S)-1   
h,t = 0,0
prod = 1
for j in T:
    prod *= alpha[j.lower()]
while S[t] not in T:
    t += 1
cur = alpha[S[t].lower()]
h = t
for i in range(len(T)):
    h += 1
    cur *= alpha[S[h].lower()]
while t < h:
    while S[h] not in T and h < end:
        h+=1
    cur *= alpha[S[h].lower()]
   # if cur % prod == 0:
    d[(h-t)+1]=[t,h]
    cur /= alpha[S[t].lower()]
    t += 1
    while S[t] not in T and t < h:
        t += 1
    cur *= alpha[S[t].lower()]

ind = d[min(d)]
print d
print S[ind[0]:ind[1]]
