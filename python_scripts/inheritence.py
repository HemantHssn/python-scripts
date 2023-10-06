class person:
    print("-----------")
    def __init__(self):
        self.f_name = "hemanth"
        self.l_name = "r"
        return None
    
    def printname(self):
        print(f"First name: {self.f_name} \nLast name : {self.l_name}")
        return None

    def __str__(self):
        
        return f"{self.f_name}"


print("--->>> this is the parent class data <<<---")

info = person()
print(info)
print(info.f_name)
print(info.l_name)

info.f_name = "HEMANTH"
info.l_name = "R"
info.printname()


print("--->>> this is the child  class data <<<---")
class student(person):
    def __init__(self):
        self.age = 23
        info.f_name = "vinay"
        info.l_name = "ck"
        print("-----------")
    def __str__(self):
        return f"{self.f_name}"
    
        pass


bio_data = student()
print(bio_data.age)
info.printname()



