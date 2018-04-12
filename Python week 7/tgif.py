count = 0 
for i in range(1,13):
    if i in [1,3,5,7,8,10,12]:
        for j in range(1,32):
            count = count + 1
            if (count-3)%7 == 0:
                print(str(j) + "." + str(i) + ".")
    elif i in [4,6,9,11]:
        for j in range(1,31):
            count = count + 1
            if (count-3)%7 == 0:
                print(str(j) + "." + str(i) + ".")
    else:
        for j in range(1,29):
            count = count + 1
            if (count-3)%7 == 0:
                print(str(j) + "." + str(i) + ".")