
def main(a):
    add = 0
    for i in range(0,len(a)):
        add += int(a[i])
    return add

if __name__ =="__main__":
    size = input()
    ar = input()
    sep_ar = ar.split(" ")
    result = main(sep_ar)
    print(result)