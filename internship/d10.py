''''
import random
player1=input('enter rock/paper/scissor;')
cpu=random.choice(['rock','paper','scissor'])
print(cpu)
if player1==cpu:
    print("it s a draw")
elif player1=='rock':
    if cpu=='scissor':
            print('player1 rocks cpu shocks')
    else:
          print('cpu rocks player1 shocks')
elif player1=='paper':
    if cpu=='rock':
            print('player1 rocks cpu shocks')
    else:
          print('cpu rocks player1 shocks')

elif player1=='scissor':
    if cpu=='paper':
            print('player1 rocks cpu shocks')
    else:
          print('cpu rocks player1 shocks')
else:
        print('There is a type error in response entered tried again')

''''''
#example
import smtplib
import random
#from smtplib import SMTP
recpt=input('enter to mail')
otp=random.randint(12422,999999)
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('jahnavipasupuleti1302@gmail.com','fxuribaetdwmodge')
server.sendmail('jahnavipasupuleti1302@gmail.com',
                recpt,
                'The otp is-'+str(otp))
server.close()
print('mail sent')
otp2=int(input('enter otp'))
if otp==otp2:
    print('The otp is valid')
else:
    print('invalid otp -check your eye right')
'''
#another example
import time
import random
for i in range(2):
    otp=random.randrange(123456,999999)
    print(otp)
    time.sleep(10)


  
                
                

    
                
