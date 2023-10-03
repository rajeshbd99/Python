#break and continue

for i in range (12):
    if (i==10):
        break #break use for terminate the loop
    print("5 X",i+1,"=",5*(i+1))
print("Loop Terminated")


for i in range(15):
    if (i==10):
        print("Skip the termination")
        continue #continue use for skip the loop
    print("5 X",i+1,"=",5*(i+1))
    
    