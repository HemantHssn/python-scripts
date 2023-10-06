def my_fun(n,lst):
    last = 0
    arr = []
    for i in lst:
        if lst[0][0] == 1:
            idx = ((lst[i][1]^last) % n)
            arr.append(arr[idx])
        else:
            idx = ((lst[1]^lst) % n)
            arr[idx][1]
    return None



if __name__ == "__main__":
    size = input()
    size_str = size.split(" ")
    size_int = [eval(i) for i in size_str]
    n = size_int[0]
    arr = size_int[1]
    lst = []
    for i in range(arr):
        ip_arr = input()
        ip_arr_str = ip_arr.split(" ")
        ip_arr_int = [eval(i) for i in ip_arr_str]
        lst.append(ip_arr_int)
    # print(lst)
    value = my_fun(n,lst)
    