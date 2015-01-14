#!/usr/bin/env python

start = 'hit'
end = 'cog'
dict = ['hot','dot','dog','lot','log']
wl = len(start)
w_check = wl - 1
dl = len(dict)

print 'dict:', dict

start_list =[]
letter_match = 0 

for word in dict:
    for i in range(wl):
        if word[i] ==  start[i]:
            letter_match += 1
    if letter_match == w_check:
        start_list.append(word)
    letter_match = 0

print 'start_list:',start_list

end_list =[]
letter_match = 0

for word in dict:
    for i in range(wl):
        if word[i] ==  end[i]:
            letter_match += 1
    if letter_match == w_check:
        end_list.append(word)
    letter_match = 0
print 'end_list:', end_list


graph = [[0 for i in dict] for i in dict]

   
print 'Graph:'
for v in graph:
    print v

letter_match = 0

for i in range(dl-1):
    for j in range((i+1),dl):
        word = dict[i]
        comp = dict[j]
        for k in range(wl):
            if word[k] == comp[k]:
                letter_match += 1
        if letter_match == w_check:
            graph[i][j] = 1
        letter_match = 0

print 'Graph:'
for v in graph:
    print v

