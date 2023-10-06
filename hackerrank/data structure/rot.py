def rot(arr,y,d):
   
    for i in range(d): 
        arr.reverse()
        a = arr[-1]
        b = arr[0:y]
        b.reverse()
        b.append(a)
        arr = b

    return arr
            
if __name__ == "__main__":
    size_no_rot = input()
    size_lst = size_no_rot.split(" ")
    size_lst_int = [eval(i) for i in size_lst]
    y = size_lst_int[0] - 1
    d = size_lst_int[1]
    user_ip = input()
    arr = user_ip.split(" ")
    value = rot(arr,y,d)
    print(*value)
