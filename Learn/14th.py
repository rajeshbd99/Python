# list in python

# list is a collection which is ordered and changeable. Allows duplicate members.

# create a list
mylist = ["apple", "banana", "cherry"]
print(mylist)

# access items

mylist = ["apple", "banana", "cherry"]
print(mylist[1])

# change item value

mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)

# loop through a list

mylist = ["apple", "banana", "cherry"]

for x in mylist:
    print(x)
    
# check if item exists

mylist = ["apple", "banana", "cherry"]
if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")

# list length

mylist = ["apple", "banana", "cherry"]
print(len(mylist))

# add items

mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)

# insert items

mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "orange")
print(mylist)

#list genarate
lst= [i for i in range(10)]
print(lst);

lst= [i*i for i in range(20) if i%2==0]
print(lst);

# remove item

mylist = ["apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)

l=[11,45,1,2,4,6,2,5,3,6,9,3,2]
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print(l.count(2))

#copy

l1=l.copy()
l1[0]=100
print(l1)

#extend
x=[100,200,300]
l1.extend(x)
print(l1)

#insert
l1.insert(1,10)
print(l1)

#pop
l1.pop()
print(l1)
