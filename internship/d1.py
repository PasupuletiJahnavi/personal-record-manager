Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> float(a)
5.0
>>> v1="5.6"
>>> int(v1)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(v1)
ValueError: invalid literal for int() with base 10: '5.6'
>>> float(v1)
5.6
>>> v2=float(v1)
>>> v2
5.6
>>> int(v2)
5
>>> print("janu")
janu
>>> name=input()
janu
>>> name=input("what is your name ?:")
what is your name ?:janu
>>> name
'janu'
>>> type(name)
<class 'str'>
>>> value=input("Enter some value : ")
Enter some value : 5.89
>>> type(value)
<class 'str'>
