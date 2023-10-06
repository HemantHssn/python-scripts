name=input("enter your name :\n")
print("hey , welcome to VSC,now you can calculate your age very easily.......!!!!!!! \n it's nice to see you here ",name)

current_year=int(input(print("enter the current year:\n")))
your_birth_year = int(input(print("enter your birth year: \n")))

age = current_year - your_birth_year 

print(age)
print("you are",age,"year old")
print(f"you are a {age} year old")
 
age_as_str= str(age)
print("your age is " +  age_as_str)


