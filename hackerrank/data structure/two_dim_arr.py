


def hour_glass(lst):
    sum = -100000000000000
    for i in range(1,5):
        for j in range(1,5):         
            res = lst[i][j] + lst[i-1][j] + lst[i-1][j-1] + lst[i-1][j+1] + lst[i+1][j] + lst[i+1][j-1] +lst[i+1][j+1]
            if res > sum :
                sum = res
            else:
                pass
    
    return sum

if __name__ == "__main__":    
    '''
    in order satisfy hacker rank problem we are doing like that but if its n numbe rwith user interface we can do same with this below logic
    size = int(input())
    two_d_arr = []
    for i in range(size):
        x = input()
        y = x.split(" ")
        z = [eval(i) for i in y]
        two_d_arr.append(z) 
    
    '''
    two_d_arr =[]
    arr_1j = input()
    arr_1j_lst = arr_1j.split(" ")
    arr_1j_int = [eval(i) for i in arr_1j_lst]
    two_d_arr.append(arr_1j_int)
    # print(*arr_1j_int)
        
    arr_2j = input()
    arr_2j_lst = arr_2j.split(" ")
    arr_2j_int = [eval(i) for i in arr_2j_lst]
    two_d_arr.append(arr_2j_int)
    # print(*arr_2j_int)
        
    arr_3j = input()
    arr_3j_lst = arr_3j.split(" ")
    arr_3j_int = [eval(i) for i in arr_3j_lst]
    two_d_arr.append(arr_3j_int)
    # print(*arr_3j_int)
        
    arr_4j = input()
    arr_4j_lst = arr_4j.split(" ")
    arr_4j_int = [eval(i) for i in arr_4j_lst]
    two_d_arr.append(arr_4j_int)
    # print(*arr_4j_int)
        
    arr_5j = input()
    arr_5j_lst = arr_5j.split(" ")
    arr_5j_int = [eval(i) for i in arr_5j_lst]
    two_d_arr.append(arr_5j_int)
    # print(*arr_5j_int)
        
    arr_6j = input()
    arr_6j_lst = arr_6j.split(" ")
    arr_6j_int = [eval(i) for i in arr_6j_lst]
    two_d_arr.append(arr_6j_int)
    # print(*arr_6j_int)
    
    # print(two_d_arr)
    
    
    value = hour_glass(two_d_arr)
    print(value)
    