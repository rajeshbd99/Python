#function Arguments and retuern statements

def average(a=2,b=2):#default arguments
    print("The average is ", (a+b)/2)
    
average(1,5) 


def name(fname,mname,lname="Chowdhury"):
    print("Hello ,",fname,mname,lname)
    
name("Subir","Kumar")  

def total(*numbers):
    for i in numbers:
        return sum(numbers)

c=total(1,2,3,4,5,6,7,8,9,10)
print(c) 


 