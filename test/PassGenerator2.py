import random
a = 'qwertyuiopasdfghjklzxcvbnm'
b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
c = '1234567890'
d = '!@#$%^&*()'

all = a+b+c+d

length = int(input('введите кол-во символов: '))
passw = int(input('введите кол-во паролей: '))
for i in range(passw):
    file = open("password.txt", "a")
    password = ''.join(random.sample(all,length))
    file.write(password + "\n")
    file.close()

