#multiplication
'''
n=int(input("enter num"))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
''''''
#positional arguments
(a,b)=(5,6)
''
#default argument
(a,b=5)=(8)
''''''
#default arguments
def addition (a,b=8):
    c=a+b
    print(c)
    
addition(5,6)
addition(7)
''''''
#keyword argument
def addition(a,b):
    print("value of a: ",a)
    print("value of b: ",b)
    c=a+b
    print(c)
#addition(5,6)
addition (b=5,a=6)
''''''
#variable lenth argument
def addition(a,*b):
    print("value in b:",b)
    d=sum(b)
    c=a+d
    print("total sum of d is :",d)
    c=a+d
    print(d)
addition(5,6,7,8,9,4)
'''
#keyword length arguments
def addition(**kwargs):
    for key,value in kwargs.items():
        print("%s ==%s" %(key,value))
addition(name="sai",number="52",city="vijayawada")
              
  


 
