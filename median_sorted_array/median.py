#!/usr/bin/env python

A=[]
B=[1]

num = []
num.extend(A)
num.extend(B)
print 'Array:',num

if len(num) ==1:
    print 'Median', num[0]
    exit

cypher, not_finished, temp, store = 10, True, -1, 1

while not_finished:
    not_finished = False
    bucket_list=[[] for diget  in range(cypher)]

    for i in num:
        temp = i / store
        bucket_list[temp%cypher].append(i)
        if  not not_finished and temp >  0:
            not_finished = True
    
    index = 0
    for L in range(cypher):
        bucket = bucket_list[L]
        for number in bucket:
            num[index] = number
            index +=1

    store *= cypher

neg_split = [[],[]]
for every in num:
    if every < 0:
        neg_split[0].append(every)
    else:
        neg_split[1].append(every)
merge_split = []
for whatever in neg_split:
    merge_split.extend(whatever)
num = merge_split
print'Sorted:', num
print 'Median:'  
length = len(num)
if length % 2 == 0:
    a = length/2
    b = a - 1
    d= float(num[a] + num[b])
    d /= 2
    print d
else:
    c = length//2
    print float(num[c])


