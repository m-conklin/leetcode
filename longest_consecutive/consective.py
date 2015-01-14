#!/usr/bin/env python

num=[1,2,3,4,7,9,100,101,102,103,104,105,111,112,114,200,201,202,203,204,205,206,207,208,209,201]

list_list =[]
con_list = []
con_list.append(num[0])

for a_num in num[1:]:
    if a_num == con_list[-1]+1:
        con_list.append(a_num)

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

print return_list
