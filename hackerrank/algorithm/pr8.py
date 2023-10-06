'''
Given five positive integers, 
find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''

def main(arr):
    res = [round(float(i)) for i in arr]
    res.sort()
    sum = 0
    for num in range(len(res)):
        sum += res[num]
    max = sum - res[0]
    min = sum - res[-1]
    print(f"{min} {max}")
    
    return None

if __name__ == "__main__":
    num = input()
    arr = num.split(" ")
    main(arr)