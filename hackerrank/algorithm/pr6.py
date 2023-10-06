def main(a,b):
    pos = 0
    neg = 0
    zero = 0
    for num in range(len(b)):
        c = int(b[num])
        if c > 0:
            pos = pos + 1
        elif c < 0:
            neg = neg + 1
            pass
        else :
            zero = zero + 1
    pos_ratio = pos / a
    neg_ratio = neg / a
    zero_ratio = zero / a
    print(f"{pos_ratio}\n{neg_ratio}\n{zero_ratio}")
    return None


if __name__ == "__main__":
    size = int(input())
    arr = input()
    arr_list = arr.split(" ")
    main(size,arr_list)

