Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> h=lambda a,b:a+b
>>> h(1,2)
3
>>> square = lambda a:a**2
>>> square(78)
6084
>>> cube=lambda a:a**3
>>> cube(3)
27
>>> max(8,0,-1)
8
>>> min(23,0,7,-1)
-1
>>>  string='i am {0} doing {1} at {2}'.format('eswar','p fs','codegnan')
...  
SyntaxError: unexpected indent
>>> string='i am {0} doing {1} at {2}'.format('eswar','p fs','codegnan')
>>> string
'i am eswar doing p fs at codegnan'
>>> name='manu'
>>> org='codegnan'
>>> ins='python full stack'
>>> h=f'i am {name} doing {ins} at {org}'
>>> h
'i am manu doing python full stack at codegnan'
