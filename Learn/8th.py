#match case statement

x= int(input("Enter a number :" ))
match x:
    case _ if x<0:
        print("X is a negative number")
    case _ if x==0:
        print("X is zero")
    case _:
        print("X is a positive number")
        