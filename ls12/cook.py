import random 


ACTIONS = ['сварим', "пожарим", "тушим"]

def cook(*args, **kwargs):
    for product in args:
        print(f'{random.choice(ACTIONS)} {product}')
    print(f'{kwargs.get("sauce", "аджика")}')

cook('картофель', "помидор", "мазик", sauce="хлеб")