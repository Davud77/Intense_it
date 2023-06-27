def greet(*args, special1, **kwargs):
    print(kwargs)
    print(special1)
    for guest in args:
        print('добро пожаловать' + guest)
    print({kwargs['special']})

greet('Магомед', "Али", special1='ererferf',special='патимат')