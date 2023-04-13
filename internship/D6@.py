#farenheit to celcius
F=int(input("Enter the temp : "))
c=((F-32)/1.8)
print("The temp in celcius is : ", c)
#Factorial
f=1
n=int(input("Enter the number : "))
for i in range(1,n+1):
    f=f *i
print(f)
#sum and average
a=int(input("Enter the value1 : "))
b=int(input("Enter the value2 : "))
c=a+b
print(c)
avg=c/2
print(avg)
#divisible by 7 but not multiple of 5
for i in range(0,200):
    if i % 7== 0 and i % 5 !=0:
        print(i,"its divisible as well as not multiple with 5 ")
        
#leap year
        year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
