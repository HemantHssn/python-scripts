summer = []
difference =[]

def a_diff(y):
    difference.append(f"{y}")
    return difference
    
def a_sum(x):
    summer.append(f"{x}")
    return summer

def main(i,r1):
    row_1 = r1.split(" ")
    aii = row_1[i]
    l = i + 1
    p = -l
    ajj = row_1[p]
    sum_list = a_sum(aii)
    diff_list = a_diff(ajj)
    return sum_list,diff_list


if __name__ =="__main__":
    size = int(input())
    for i in range(size):
        r1 = input()
        diagonal = main(i,r1)
a = diagonal[0]
b =diagonal[1]
first = 0
second = 0
for num in range(len(a)):
    first += int(a[num])
    second += int(b[num])
    result = abs(first - second)

print(result)

