import math

radius = int(input("Введите радиус"))
c_lengt = round(2 * math.pi * radius, 2)
c_square = round(math.pi * radius ** 2, 2)
print("Длина окружности", c_lengt)
print("Площадь окружности", c_square)