def main(x):
    num = 0
    for num in range(x):
        num += 1
        a = " " * (x - num)
        b = "#" * num
        print(f"{a}{b}")

    return None




if __name__ == "__main__":
    size = int(input())
    main(size)
