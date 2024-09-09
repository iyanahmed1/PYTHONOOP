#write a python program to check if a number is a prime number
num=int(input('Please enter your number: '))
#variable to check f a number is a not prime number
x=False
if num ==1:
    print(f"{num},is not a prime number")
elif num>1:
    #check for factors
    for i in range(2,num):
        if(num % i)==0:
            x=True
            break
#check if x is false
    if x:
        print(f'{num}, is not a prime number')
    else:
        print(f'{num},is a prime number')

