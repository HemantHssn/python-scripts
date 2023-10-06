language=("kan","eng","hin","telg","tamil")
print(len(language))
print(language)

#tuples can't be appended but still it can be chege by other means
language=language + ("malyalam",)      #if we dont put ','here it will treet that as string and string cant be added to tuples
print("after adding few tuples :\n")
print(len(language))
print(language)

# language=language - ("malyalam",)  '''remove can't be done for tuples'''
# print("after removing few tuples :\n")
# print(len(language))
# print(language)


                                              

