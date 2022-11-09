#for loop 0 to 150

for n in range(0, 151):
    print(n, end='')

def getMultiples(num, number_of_multiples):
    i = 1
    while i <= number_of_multiples:
        print(num*i)
        i +=1
getMultiples(5,200);


for i in range(1, 101):
    if i % 10 == 0:
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)


finalSum = 0                       
for num in range(0,500000):
    if num % 2 != 0:                 
        finalSum = finalSum + num     
        print(finalSum) 

for num in range(2018,0,-4):
    print(num)
