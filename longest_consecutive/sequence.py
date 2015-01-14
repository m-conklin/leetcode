#!/usr/bin/env python

num=[1,2,0,1]
print 'Array:',num


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
        
list_list, con_list = [],[]
con_list.append(num[0])

for a_num in num[1:]:
    if a_num == con_list[-1]+1:
        con_list.append(a_num)
    elif a_num == con_list[-1]:
        x=1

    else:
        list_list.append(con_list)
        temp_list=[]
        temp_list.append(a_num)
        con_list=temp_list
list_list.append(con_list)

return_list=[]
for a_list in list_list:
    if len(a_list) > len(return_list):
        return_list = a_list

print 'Longest Sequence', return_list
print 'Length:', len(return_list)
