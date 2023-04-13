#add two numbers
'''

def  add(a,b):
    if a>b:
        return 'ais big'
    else:
        return 'b is big'
add(2,3)
''''''
#lamda
h=lambda a,b:a+b
square = lamda a:a**2
cube=lamda a:a**3
d=lamda lst:max(lst)
h(1,2,4,5)
''''''
#string to list
k=input('enter numbers with spaces')
print(k.split())
l=[]
for i in k.split():
    l.append(int(i))
print(l,b-a)
'''''''
def square(a):
    return a**a
st=[2,9,8,7]
lst2=[]
for i in lst:
     lst2.append(square(i))
print(lst2)
k=tuple(map(int,input('enterb number with spaces').split()))
print(k)

#another method list using map
lst=list(map(int,input('enter number with spaces').split()))
new_lst=list(map(square,lst))
print(new_lst)
''''''
k=list(map(int,input('enter numbers with sp').split()))
new_list=list(filter(lambda x:x%2==0,k))
print(new_list)
''''''''
h=lambda a,b:a+b
h(1,2)
3
square = lambda a:a**2
square(78)
6084
cube=lambda a:a**3
cube(3)
27
max(8,0,-1)
8
min(23,0,7,-1)
-1n 
''''
string='i am {0} doing {1} at {2}'.format('eswar','p fs','codegnan')
string
name='manu'
org='codegnan'
ins='python full stack'
h=f'i am {name} doing {ins} at {org}'
h




