class Myclass(object):

    def __init__(self, user_string):
        self.char_frequency = {}

        for char in user_string:
            self.char_frequency[char] = self.char_frequency.get(char, 0) + 1

        count = 0
  
        for key in self.char_frequency:
            value = self.char_frequency[key]
            if value == 1:
               count += 1
        print(count)
        return None


input = Myclass(str(input()))




