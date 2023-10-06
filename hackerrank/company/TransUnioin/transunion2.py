def main(user_string):
    char_frequency = {}

    for char in user_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    count = 0
  
    for key in char_frequency:
        value = char_frequency[key]
        if value == 1:
            count += 1

    return count


if __name__ == "__main__":
   user_string = str(input())
   result = main(user_string)
   print(result) 


'''def main(user_string):
    char_frequency = {}

    for char in user_string:
        print(char)
        char_frequency[char] = char_frequency.get(char, 0) + 1
        print(char_frequency)
        print(char_frequency[char])

    count = 0
    for char, frequency in char_frequency.items():
        if frequency == 1:
            count += 1

    return count


if __name__ == "__main__":
   user_string = str(input())
   result = main(user_string)
   print(result)

'''

"""

from collections import Counter

def main(compString):
    char_frequency = Counter(compString)
    count = 0

    for char in compString:
        if char_frequency[char] == 1:
            count += 1

    return count

if __name__ == "__main__":
   compString = str(input())
   result = main(compString)
   print(result)


"""