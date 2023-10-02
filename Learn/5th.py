#string

name = "Rajesh"
friend = "Rohan"

anotherfriend = "Srikanto"

dialouge = """I am Rajesh
I am a student of B.Sc in CSE
I am from Bangladesh
I am a student of KIIT School of Computer Engineering
"""
print("Hello "+name)
print("Hello "+friend)
print("Hello "+anotherfriend)
print(dialouge)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print(name[0:3]) # 0 to 2
print(name[0:-2]) # 0 to 4 

for character in dialouge: # for loop is used to print each character of a string
    print(character)
    
print(len(dialouge)) # len() function is used to find the length of a string