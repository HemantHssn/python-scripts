str = input()
word = input()
indices = str.split(word)
# print(indices)
my = []
y = len(indices) - 1
for i in range(y):
    pos = len(indices[i])
    if i >= 1:
        a = i - 1
        # print(my[a])
        c = pos + my[a] + len(word)
        # print(c)
        my.append(c)
    else :
        pos = pos + 1
        my.append(pos)
      
print(*my)
# manoj hemanth samanth manjunanth man --->>> first & last         --->>> last number has to be deleted <<<---
# hemanth manoj samanth manjunanth --->>> niether first nor last   --->>> last number has to be deleted <<<---
# manoj hemanth samanth manjunanth --->>> only first               --->>> last number has to be deleted <<<---
# hemanth manoj samanth manjunanth man --->>> only last            --->>> last number has to be deleted <<<---
