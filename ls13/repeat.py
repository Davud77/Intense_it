def simple_func(*args, **kwargs):
    print(args)
    print(kwargs)

simple_func(1, 2, 3, x="qweqerew", y='rfegrth')

num_list = [1, 2, 3, 4]
print(list(filter(lambda x:x > 2, num_list)))
print(list(map(lambda x:x * 2, num_list)))