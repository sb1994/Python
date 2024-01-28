# def hypervolume(*args):
#     print(args)
#     print(type(args))


def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v
    # print(type(args))


print(hypervolume(3, 4))
hypervolume(3, 4, 5)
