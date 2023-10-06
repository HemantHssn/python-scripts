


if __name__ == "__main__":
    size = input()
    arr = input()
    arr_upd = arr.split(" ")
    # print(arr_upd)
    arr_list = [eval(i) for i in arr_upd]
    # print(arr_list)
    # arr_list.sort()
    arr_list.reverse()
    # print(arr_list)
    # for i in xrange(arr_list):
    #     print(arr_list[i], end =" ")
    print(*arr_list)
    
    
    # str = ["hemanth","r"]
    # print(*str)