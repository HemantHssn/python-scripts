contactdict ={"appaji":9663663129,"chethan anna":7845430156,"preetham raj":7022217644}
class Contact(object):    
    def __init__ (self, name, number):
        print("entered to contact form")
        self.name = name
        self.number = number
        print("exiting from contact form")
        self.contact_dictionary()

    def contact_dictionary(self):
        self.key = self.name
        self.value = self.number
        contactdict[self.key] = self.value
        print(contactdict)
    
    pass

choice1 = input("add or search\n")

if choice1 == "add":
    user = Contact("hemanth","8951131968")
    user.name = input("Enter Your Name :\n")
    user.number = input("Enter The Number :\n")
    user.contact_dictionary()
        
    
elif choice1 == "search":
    choice2 = input("serarch by name or number:\n")
    if choice2 == "name" :
        hesaru = input("Enter The Name:\n")
        print(contactdict[hesaru])
    
    elif choice2 == "number":
        dial = input("Enter The Phone Number:\n")
        for key,val in contactdict.items():
            if val == dial:
                print(key)
        

    

