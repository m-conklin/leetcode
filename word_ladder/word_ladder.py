#!/usr/bin/env python

start = 'hit'
end = 'cog'
dict = ['hot','dot','dog','lot','log']
word_length = len(start)

start_list =[]
letter_match = 0 

for word in dict:
    for i in range(len(word)):
        if word[i] ==  start[i]:
            letter_match += 1
    if letter_match == len(word)- 1:
        start_list.append(word)
    letter_match = 0

print 'start_list:',start_list

end_list =[]
letter_match = 0

for word in dict:
    for i in range(len(word)):
        if word[i] ==  end[i]:
            letter_match += 1
    if letter_match == len(word)- 1:
        end_list.append(word)
    letter_match = 0
print 'end_list:', end_list



