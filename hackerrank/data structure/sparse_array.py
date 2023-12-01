
def str(a):
    str_lst = []
    for i in range(a):
        word = input()  #f"enter the {i} str_word : "
        # print(str_lst)
        # print(word)
        str_lst.append(word)
        # print(str_lst)
        

    return str_lst

def querry(a):
    query_lst = []
    for i in range(a):
        word = input() #f"enter the {i} query_word : "
        # print(query_lst)
        # print(word)
        query_lst.append(word)
        # print(query_lst)    


    return query_lst


def solution(a,b):
    ans = []
    for query in b:
        count = 0
        for str in a:
            if str == query:
                count = count +1
            else:
                pass
        ans.append(count)
    return ans

if __name__ == "__main__":
    str_size = int(input()) #"enter the size: "
    final_str = str(str_size)
    quer_size = int(input()) #"enter the size of queri : "
    final_quer = querry(quer_size)
    display = solution(final_str,final_quer)
# print(final_str)
# print(final_quer)
print(*display,sep = "\n")

