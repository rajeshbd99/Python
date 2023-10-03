#functions

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print(a, "is greater than",b)
    elif(a==b):
         print(a, "is equal to",b)
    else:
        print(a, "is less than",b)    
    
a=9
b=8
calculateGmean(a,b)
isGreater(a,b)

c=8
d=7
calculateGmean(c,d)
isGreater(c,d)

#list of all built in function in python
#https://docs.python.org/3/library/functions.html

