#!/usr/bin/env python

A=[100,4,200,1,3,2]


cypher, not_finished, temp, store = 10, True, -1, 1

while not_finished:
    not_finished = False
    bucket_list=[[] for diget  in range(cypher)]

    for i in A:
        temp = i / store
        bucket_list[temp%cypher].append(i)
        if  not not_finished and temp > 0:
            not_finished = True
    
    index = 0
    for L in range(cypher):
        bucket = bucket_list[L]
        for number in bucket:
            A[index] = number
            index +=1

    store *= cypher

print A
