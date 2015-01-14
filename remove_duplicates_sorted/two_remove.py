#!/usr/bin/env python

A=[1,2,3,4]

if len(A) in [0,1]:
    print len(A)


if len(A) == 2 and A[0] == A[1]:
    print 'same'
elif len(A) == 2 and A[0] != A[1]:
     print 'diff'

r,i = 1,2
end = len(A)
s = False 

while i < end:
    if A[r] > A[r-1]:
        r += 1
        i +=1
    elif A[i] > A[r] and A[i] > A[r-1]:
        A[r],A[i] = A[i],A[r]
        r += 1
        i += 1
        s = True
    else:
        i +=1
        s = True

if A[r] == A[r-1]:
    s = True

print A
print 'R:',r
print 'S:',s
