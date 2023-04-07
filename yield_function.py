# using multiple yields in a function to create a single list of two seperate lists

def mul_yield(x, y):    # this creates a generator object containing two elements in a single list
    for i in range(len(x)):
        yield (x[i])
        yield (y[i])     # This yield is called after the first next and then passes on to the first yield


def list_gen(x_y):       # iterating over the generator object and appending the elements into a list
    gen_list = []
    for i in x_y:
        gen_list.append(i)
    return gen_list


list1 = [1, 5, 10, 15, 20]
list2 = [2, 4, 6, 8, 10]

yield_mul = mul_yield(list1, list2)

print(yield_mul)

merge_list = list_gen(mul_yield(list1, list2))

print(merge_list)