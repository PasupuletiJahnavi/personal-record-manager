Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=[1,2,3,4,5,6,7,8]
for i in num:
    print(i)

    
1
2
3
4
5
6
7
8
import time
num=[1,2,3,4,5,6,7,8]
for i in num:
    print(i)
    
SyntaxError: multiple statements found while compiling a single statement
import time
num=[1,2,3,4,5,6,7,8]
for i in num:
    print(i)
    time.sleep(2)
    
SyntaxError: multiple statements found while compiling a single statement

============================================ RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py ===========================================
1
2
3
4
5
6
7
8

============================================ RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py ===========================================
3
6

============================================ RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py ===========================================
3
Enter year to be checked:1990
6
Enter year to be checked:2003
The year isn't a leap year!

============================================ RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py ===========================================
3
Enter year to be checked:2004
6
Enter year to be checked:2004
The year is a leap year!
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py", line 15, in <module>
    fahrenheit = (celsius * 1.8) + 32
NameError: name 'celsius' is not defined

============================================ RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py ===========================================
3
Enter year to be checked:2003
6
Enter year to be checked:2004
The year is a leap year!
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py", line 15, in <module>
    fahrenheit = (celsius * 1.8) + 32
NameError: name 'celsius' is not defined

============================================ RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py ===========================================
3
Enter year to be checked:2003
6
Enter year to be checked:2004
The year is a leap year!
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/d6.py", line 15, in <module>
    Celsius = ((Fahrenheit-32)*5)/9
NameError: name 'Fahrenheit' is not defined

=========================================== RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/D6@.py ===========================================
Enter the temp : 12
The temp in celcius is :  -11.11111111111111

=========================================== RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/D6@.py ===========================================
Enter the temp : 13
The temp in celcius is :  -10.555555555555555
Enter the number : 121
809429852527344373968162284544935082997082306309701607045776233628497660426640521713391773997910182738287074185078904956856663439318382745047716214841147650721760223072092160000000000000000000000000000

=========================================== RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/D6@.py ===========================================
Enter the temp : 14
The temp in celcius is :  -10.0
Enter the number : 2
2
Enter the value1 : 12
Enter the value2 : 13
25
12.5
>>> 
=========================================== RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/D6@.py ===========================================
Enter the temp : 23
The temp in celcius is :  -5.0
Enter the number : 2
2
Enter the value1 : 3
Enter the value2 : 4
7
3.5
7 its divisible as well as not multiple with 5 
14 its divisible as well as not multiple with 5 
21 its divisible as well as not multiple with 5 
28 its divisible as well as not multiple with 5 
42 its divisible as well as not multiple with 5 
49 its divisible as well as not multiple with 5 
56 its divisible as well as not multiple with 5 
63 its divisible as well as not multiple with 5 
77 its divisible as well as not multiple with 5 
84 its divisible as well as not multiple with 5 
91 its divisible as well as not multiple with 5 
98 its divisible as well as not multiple with 5 
112 its divisible as well as not multiple with 5 
119 its divisible as well as not multiple with 5 
126 its divisible as well as not multiple with 5 
133 its divisible as well as not multiple with 5 
147 its divisible as well as not multiple with 5 
154 its divisible as well as not multiple with 5 
161 its divisible as well as not multiple with 5 
168 its divisible as well as not multiple with 5 
182 its divisible as well as not multiple with 5 
189 its divisible as well as not multiple with 5 
196 its divisible as well as not multiple with 5 
>>> 
=========================================== RESTART: C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/D6@.py ===========================================
Enter the temp : 1
The temp in celcius is :  -17.22222222222222
Enter the number : 2
2
Enter the value1 : 3
Enter the value2 : 4
7
3.5
7 its divisible as well as not multiple with 5 
Enter year to be checked:2004
14 its divisible as well as not multiple with 5 
Enter year to be checked:2005
21 its divisible as well as not multiple with 5 
Enter year to be checked:2345
28 its divisible as well as not multiple with 5 
Enter year to be checked:
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/AppData/Local/Programs/Python/Python311/D6@.py", line 24, in <module>
    year=int(input("Enter year to be checked:"))
ValueError: invalid literal for int() with base 10: ''
