import random
import time

a = 'qwertyuiopasdfghjklzxcvbnm'
b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
c = '1234567890'
d = '!@#$%^&*()'

all = a+b+c+d

length = int(input('введите кол-во символов: '))
password = ''.join(random.sample(all,length))
print("идет генерация пароля")
time.sleep(2)
print("Ваш пароль:", password)