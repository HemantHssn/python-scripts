
# array manipulation
def sol(array_2d):
    # result_dict = {}
    max_sum = 0
    for j in range(len(array_2d[0])):
        column_elements_sum = sum([array_2d[i][j] for i in range(len(array_2d))])
        # result_dict[str(j+1)] = column_elements_sum
        
        if column_elements_sum > max_sum:
            max_sum = column_elements_sum

    return max_sum


def cal(arr,n,m):
    fin_arr = []
    sub_arr = []
    for lst in arr:
        a = int(lst[0])
        b = int(lst[1])
        k = int(lst[2])
        for i in range(0,a-1):
            sub_arr.insert(i,0)
        for i in range(a,b+1):
            sub_arr.insert(i,k)
        for i in range(b+1,n+1):
            sub_arr.insert(i,0)
        fin_arr.append(sub_arr)
        sub_arr = []
    # print(fin_arr)
        
    # result = sol(fin_arr)
        
    return sol(fin_arr)


if __name__ == "__main__":
    # n_m = input(f"enter the space seperated size_operation:\n").split()
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n <= 10**7 and 3 <= n:
        if m <= 2*10**5 and 1<=m:
            arr = []
            for i in range(m):
                
                # abc = input(f"enter the space seperated a_b_k array elements:\n").split()
                abc = input().split()
                a = int(abc[0])
                b = int(abc[1])
                k = int(abc[2])

                
                # print(f"this is the abc array:\n{abc}")
                if 1<=a and a<=b and b<=n :
                    if 0<=k and k<=10**9:
                        # print(f"this is the a_b_k array:\n{abc}")
                        arr.append(abc)
            # print(arr)
    result = cal(arr,n,m)
    print(result)
    # print(f"this is the final answer:\n{result}")




'''
10 3
1 5 3
4 8 7
6 9 1


5 3
1 2 100
2 5 100
3 4 100

'''


'''
for i in range(1,5+1):
    print(i)
    
'''



''''
    my_dict = {}
    my_dict["1"] = [1,2,3,4]
    my_dict["2"] = [5,6,7,8]
    my_dict["3"] = [9,10,11,12]
    print(my_dict)

'''