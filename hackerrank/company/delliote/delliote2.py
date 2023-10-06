my_dict = {}
arr_1 = input()
arr_1_lst = arr_1.split(" ")
arr_1_lst_int = [eval(i) for i in arr_1_lst]
for item in arr_1_lst_int:
    my_dict[item] = my_dict.get(item,0) + 1

arr_2 = input()
arr_2_lst = arr_2.split(" ")
arr_2_lst_int = [eval(i) for i in arr_2_lst]
for item in arr_2_lst_int:
    my_dict[item] = my_dict.get(item,0) + 1

arr_3 = input()
arr_3_lst = arr_3.split(" ")
arr_3_lst_int = [eval(i) for i in arr_3_lst]
for item in arr_3_lst_int:
    my_dict[item] = my_dict.get(item,0) + 1


for key in my_dict:
    value = my_dict[key]
    if value == 3:
        print(key)


print(my_dict)