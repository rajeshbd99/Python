#string methods in python

name = "!!!! !Rajesh! !!!!!!"
print(name.upper()) # upper() method is used to convert a string into uppercase
print(name.lower()) # lower() method is used to convert a string into lowercase

print(name.rstrip("!")) # rstrip() method is used to remove the character from the right side of the string

print(name.replace("Rajesh","Rohan")) # replace() method is used to replace a character or a string with another character or string

print(name.split(" ")) # split() method is used to split a string into a list of strings

heading = "python is a prograMming languAge"
print(heading.capitalize())# capitalize() method is used to capitalize the first letter of the string
print(heading.center(50," "))# center() method is used to center align the string
print(len(heading))
print(len(heading.center(50," ")))


print(heading.count("n")) # count() method is used to count the number of times a character or a string is repeated in a string

print(heading.endswith("** ")) # endswith() method is used to check whether the string ends with a particular character or string

print(heading.find("a")) # find() method is used to find the index of a character or a string in a string

print(heading.index("is")) # index() method is used to find the index of a character or a string in a string

print(heading.isalnum()) # isalnum() method is used to check whether the string is alphanumeric or not

print(heading.islower())

print(heading.isspace()) # isspace() method is used to check whether the string contains only spaces or not

print(heading.swapcase())# swapcase() method is used to swap the cases of the string

print(heading.startswith("python")) # startswith() method is used to check whether the string starts with a particular character or string

print(heading.istitle())# istitle() method is used to check whether the string is in title case or not

print(heading.title())# title() method is used to convert the string into title case