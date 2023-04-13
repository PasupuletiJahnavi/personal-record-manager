
























  /.??5 Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=123456789
print(int(str(num)[::-1]))
987654321
type(num)
<class 'int'>
a=('python','saketh',25,'codegnan',36,'mentor',[1,4,5],26)
a[1:8:2]
('saketh', 'codegnan', 'mentor', 26)
 a='ppy!'
 
SyntaxError: unexpected indent
a='ppy!'
print(a[0]+'a'+a[1]+'a'+a[3])
papa!
print(a[0]+'a'+a[1]+'a'+a[2]+'a'+a[3])
papaya!
'a'.join(a)
'papaya!'
a=["I","work","i","code"]
b=["am","ing","n","gnan"]
c=a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+a[3]
c
'I am working in codecode'
c=a[0]+" "+b[0]+" "+a[1]+b[1]+" "+a[2]+b[2]+" "+a[3]+b[3]
c
'I am working in codegnan'
p=['a','b',['c',['d','e',['f', 'g'], 'k'], 'l'], 'm','n']
p
['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
p[2]
['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
p[2][1]
['d', 'e', ['f', 'g'], 'k']
p[2][1][1]
'e'
p[2][1][2]
['f', 'g']
p[2][1][2]=['f','g','h','i']
p[2][1][2]
['f', 'g', 'h', 'i']
p
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i'], 'k'], 'l'], 'm', 'n']
m='Ivis'
n='code'
m[0]+n[-1]+m[1]+n[-2]+m[2]+n[-3]+m[3]+n[-4]
'Ievdiosc'
k='I work in codegnan and codegnan is in vijayawada and love codegnan'
k.count()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    k.count()
TypeError: count() takes at least 1 argument (0 given)

k.count('codegnan')
3
k='I work in Codegnan and codegnan is in vijayawada and love codegnan'
k.count('codegnan')
cv //./// 2
k.lower()
'i work in codegnan and codegnan is in vijayawada and love codegnan'
k.count('codegnan')
2
m='I work in Codegnan and codegnan is in vijayawada and love codegnan'
m.count('codegnan')
2
m.lower()
'i work in codegnan and codegnan is in vijayawada and love codegnan'
m.count('codegnan')
2
f=m.lower()
f.count('codegnan')
3
g="saketh-is-a-python-mentor"
b=a.split('-')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b=a.split('-')
AttributeError: 'list' object has no attribute 'split'
>>> b=g.split('-')
>>> b
['saketh', 'is', 'a', 'python', 'mentor']
>>> w="python learning am I"
>>> b=w.split(' ')
>>> b
['python', 'learning', 'am', 'I']
>>> b=w[-1]+w[-2]+w[-3]+w[-4]
>>> b
'I ma'
>>> b=b[-1]+b[-2]+b[-3]+b[-4]
>>> b
'am I'
>>> w="python learning am I"
>>> b2=w.split(' ')
>>> c=b2[-1]+' '+b2[-2]+' '+b2[-3]+' '+b2[-4]
>>> c
'I am learning python'
>>> a='silent'
>>> a=[-4:-6]
SyntaxError: invalid syntax
>>> a[-4:-6]
''
>>> a
'silent'
>>> a[-5:-1]
'ilen'
>>> -a[-5:]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    -a[-5:]
TypeError: bad operand type for unary -: 'str'
>>> a[-5:]
'ilent'
>>> a[-5:0]
''
>>> a
'silent'
