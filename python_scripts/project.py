build_name = "FHGW23R2_010.1.9_2303022258_1430293_base"

''''slicing method'''
print(''''\nslicing method''')
print("build_name = ",build_name)
rislable = build_name[0:16]
print(type(rislable),rislable)

revision = build_name[28:35]
print(type(revision),revision)

'''converting string to list method'''
print('''\nconverting string to list method''')
print("build_name = ",build_name)
string_breakdown = build_name.split("_")
print(string_breakdown)
index_1 = string_breakdown[0]
index_2 = string_breakdown[1]
rislable = f'{index_1}_{index_2}'
print(type(rislable),rislable)
print("-------------")
print('_'.join(string_breakdown[0:2]))
print("--------------")
revision = string_breakdown[3]
print(type(revision),revision)




'''coming into list'''
print('''coming into list''')
print("build_name = ",build_name)
build_name_as_list = build_name.split("_")
print(build_name_as_list)
index_1 = [f"{build_name_as_list[0]}_{build_name_as_list[1]}",build_name_as_list[3]]
print(len(index_1))
print(type(index_1),index_1)
index_1 = [f"{build_name_as_list[0]}_{build_name_as_list[1]}"]
index_1.append(build_name_as_list[3])
print(len(index_1))
print(type(index_1),index_1)



'''coming into dictionary'''
print("\n'''coming into dictionary'''")
print("build_name = ",build_name)
string_breakdown = build_name.split("_")
index_1 = string_breakdown[0]
index_2 = string_breakdown[1]

rislable_value = f'{index_1}_{index_2}'

revision_value = string_breakdown[3]

my_dict = {'rislable': rislable_value,'revision': revision_value}
print(my_dict)
print(type(my_dict),my_dict)
print(my_dict['rislable'])   # print(my_dict.get('rislable'))
print(my_dict['revision'])

