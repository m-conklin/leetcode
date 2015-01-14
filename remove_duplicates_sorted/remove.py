#!/usr/bin/env python

A=[1,1,2,2,3]

if len(A) in [0,1]:
    print len(A)

a,b,c = 0,1,2

if len(A) == 2 and A[a] == A[b]:
    print 'same'
elif len(A) == 2 and A[a] != A[b]:
     print 'diff'


end = len(A)
while c < end:
    if A[a] < A[b]:
        a += 1
        b += 1
        c += 1
    elif A[c] <=  A[b] or A[c] <= A[a]:
        c +=1
    else:
        A[b],A[c] = A[c],A[b]

print A
print b
