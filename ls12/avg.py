# def avg(num_list):
#     return sum(num_list) / len(num_list)

# print(avg([1, 4, 6, 67, 45535]))


def avg(*args):
    return sum(args) / len(args)

print(avg(4, 5, 84))