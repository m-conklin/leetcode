#!/usr/bin/env python

words = ["What","must","be","shall","be."]
L = 12

if L == 0 or L ==1:
    print words

line = []
line_list= []
line_length = 0
empty = True

for word in words:
    if empty:
        line.append(word)
        line_length += len(word)
        empty = False
    elif len(word) + 1 + line_length <= L:
        line.append(word)
        line_length += (len(word) + 1)
    else:
        line_list.append(line)
        temp = []
        temp.append(word)
        line = temp
        line_length = len(word)

line_list.append(line)

print line_list
for each_line in line_list[:-1]:
    characters = sum(len(string) for string in each_line)
    to_add = L - characters
    spaces = len(each_line) - 1

    if spaces in [0,1]:
        add_first = " "*to_add
        each_line[0] += add_first
    else:
        for i in range(len(each_line)-1):
            sp = to_add/spaces
            if to_add%spaces!= 0 and i < to_add%spaces:
                sp += 1
            add = " "*sp
            each_line[i] += add

last_line = line_list[-1]

for j in range(len(last_line[:-1])):
    last_line[j] += " " 
last_char = sum(len(string) for string in last_line)
app = " "*(L - last_char)
last_line[-1] += app 

line_list =[''.join(line) for line in line_list]

print line_list
