#tuples

tup = (1,2,3,4,5,6,7,8,9,10)
print(type(tup),tup)

print(tup[3])
print(tup[3:6])
print(tup[3:6:2])
print(tup[-2])

#tuple is immutable but we can change it by converting it into list and then again into tuple 
temp = list(tup)
temp.append(11)
temp.append(12)
temp.pop()
tup = tuple(temp)
print(tup)

#count

tuple = (1,2,3,2,4,5,3,6,4,6,9,6,4,6,8,4)
res = tuple.count(6)
print(res)


