number = int(input('Enter the number: '))
l1=[]
for i in range(2,number+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        l1 +=[i]
print(l1)