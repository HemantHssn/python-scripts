n = int(input("enter the size you required tohave the pattern: \n"))

print("====== pattern : 1 ======")
for i in range(n):
    pattern = i*"   " + (n-i)*" * " 
    print(pattern)

print("====== pattern : 2 ======")
for i in range(n):
    i += 1
    pattern = i*" * "
    print(pattern)

# print((n+1)*" * ")
print("====== pattern : 3 ======")
for i in range(n):
    pattern = (n-i)*" * " + i*"   "
    print(pattern)

print("====== pattern : 4 ======")
for i in range(n):
    i += 1
    pattern = (n-i)*"   " + i*" * "
    print(pattern)
