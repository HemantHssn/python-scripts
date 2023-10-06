def self_divide(num):
    left = num
    while left:
        remainder = left % 10
        if remainder == 0 or num % remainder != 0:
            return False
        left //= 10
    return True

def self_dividing_numbers(left, right):
    result = []
    for i in range(left, right + 1):
        if self_divide(i):
            result.append(i)
    return result

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def solve(N, words, S):
    min_distance = float('inf')
    best_word = ''

    for word in words:
        distance = levenshtein_distance(word, S)
        if distance < min_distance or (distance == min_distance and word < best_word):
            min_distance = distance
            best_word = word

    return best_word

# Example usage:
N = int(input())
words = input().split()
S = input()
out = solve(N, words, S)
print(out)



