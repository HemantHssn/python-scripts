def minimum_horseshoes(s1, s2, s3, s4):
    unique_colors = set([s1, s2, s3, s4])
    # print(type(unique_colors))
    # print(unique_colors)
    return 4 - len(unique_colors)

s1, s2, s3, s4 = map(int, input().split())
result = minimum_horseshoes(s1, s2, s3, s4)
print(result)





# data = set([1,2,3,2],)
# print(type(data))
# print(data)