def solve(start, stop):
    s = 0
    for n in range(start, stop+1):
        temp = n
        flag = 0
        while(n):
            k = n % 10
            if k==0 or (temp % k != 0):
                flag = 1
                break
            n //= 10
        if flag==0:
            s += temp
           
    return s

start = int(input())
stop = int(input())
out = solve(start, stop)

print(out)
  