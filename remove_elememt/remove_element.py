#!/usr/bin/env python

A = [3,3]

elem =5 

r = 0
end = len(A) - 1

if len(A) == 0:
    print '0'

while True:
    if r >= end:
     break

    if A[r] != elem:
        r +=1
    elif A[r] ==  elem and A[end] == elem:
        end -= 1
    else:
        A[r],A[end] = A[end],A[r]
        r += 1

print A
print 'R:', r
