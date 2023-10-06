def count_specific_digit(data, digit):
    data_str = str(data)
    count = 0

    for char in data_str:
        if int(char) == digit:
            count += 1

    return count

data = int(input())
digit = int(input())
result = count_specific_digit(data, digit)
print(result)
