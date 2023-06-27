def solve_eq(a=1, b=0, c=0):
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        print("У уравнения нет корней")
        return
    elif discr == 0:
        x = -b / (2 * a)
        print(f'x = {x}')
        return x
    else: 
        x1 = (-b + discr ** 0.5)/ (2 * a)           
        x2 = (-b - discr ** 0.5)/ (2 * a)
        print(f'x1 = {x1}\nx2 = {x2}')
        return x1, x2
    
solve_eq(7,-4,0) #позиционные аргументы
solve_eq(a=34455, c=0, b=34) #именованные аргументы