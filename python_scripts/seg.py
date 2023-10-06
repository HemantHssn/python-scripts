
fo = open("file.txt","r")
list = (fo.readlines())
# print(list)
for key in range((len(list))):
    name = f"{list[0]}"
    # print(name)

fo.close()

import sys

input_from_user = sys.argv[1]
frame_1 = f"{input_from_user} May"
frame_2 = f"{input_from_user}th May"

with open('file.txt', 'r') as data:
    information = data.readlines()

# print(type(information))
users_comming_on_date = {}
name_list = []

for each_item in information:
    if frame_1 in each_item or frame_2 in each_item:
        names = each_item.split('.')[1].split('-')[0]
        name_list.append(names)
val = {frame_1: name_list}
users_comming_on_date.update(val)

print(users_comming_on_date)


