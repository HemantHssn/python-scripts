no = input()
lst = no.split(" ")
lst_no = [eval(i) for i in lst]
print(lst_no)
product = lst_no[0] * lst_no[1]
sum = lst_no[0] + lst_no[1]
result = product - sum
print(result)