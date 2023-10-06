
def palindrome(a):
    if a == a[::-1]:
        x = "a" 
    else:
        x = "not a" 
    return x



if __name__ =="__main__":
    user_str = input("enter your word:\n")
    value = palindrome(user_str)
print(f"the given word :{user_str}\nThe word {user_str} is {value} palindrome")