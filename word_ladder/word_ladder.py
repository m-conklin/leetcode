#!/usr/bin/env python

start = 'hit'
end = 'cog'
dict = ['hot','dot','dog','lot','log']
wl = len(start)
w_check = wl - 1
dl = len(dict)
r_dl = range(dl)
print 'dict:', dict

start_list =[]
letter_match = 0 

for word in r_dl:
    for i in range(wl):
        if dict[word][i] ==  start[i]:
            letter_match += 1
    if letter_match == w_check:
        start_list.append(word)
    letter_match = 0

print 'start_list:',start_list
for i in start_list:
    print dict[i]

end_list =[]
letter_match = 0

for word in r_dl:
    for i in range(wl):
        if dict[word][i] ==  end[i]:
            letter_match += 1
    if letter_match == w_check:
        end_list.append(word)
    letter_match = 0
print 'end_list:', end_list
for i in end_list:
    print dict[i]

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
            graph[i][j],graph[j][i] = 1,1
        letter_match = 0

print 'Graph:'
for v in graph:
    print v

vertices = [[None,None] for word in dict]

queue = []

for start_vertex in start_list:
#    for end_vertex in end_list:
        queue.append(start_vertex)
        vertices[start_vertex][0] = 0

        while len(queue) > 0:
            dq = queue.pop(0)
            for adj in r_dl:
                if graph[dq][adj] == 1 and vertices[adj][0] == None:
                    queue.append(adj)
                    dist = vertices[dq][0] + 1
                    vertices[adj] = [dist,dq]

#        print 'end:',end_vertex, dict[end_vertex]
        print 'vert:',vertices

            
