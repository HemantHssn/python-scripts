class my_class:
    def __init__(self,hesaru):
        print("entering to __init__ method")
        self.name = hesaru
        self.age = 22
        print("exiting from __init__ method")

    def information(self):
        print(f"the user name is {self.name} and the user age  is {self.age}")

    def __str__(self):
        return f"object without properties --->>> \ name & age \ {self.name} & {self.age}"

user = my_class("hemanth")     

print(user)
print(user.name)
print(user.age)
user.information()
user.name = input("Enter your Name:\n")
user.age = input("enter ypur age:\n")
print("form geting updating")
print(user)
# del user.age
# print(f"the updated info of the user is name: {user.name}")
print(f"the updated info of the user is name: {user.name} with age :{user.age}")

