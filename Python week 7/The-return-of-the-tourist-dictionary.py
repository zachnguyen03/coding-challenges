def print_in_accordance_of_values(dct):
    new_lst = sorted(dct, key=lambda x: dct[x])
    for i in new_lst:
        print(dct[i], i)