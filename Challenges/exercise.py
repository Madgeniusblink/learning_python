def add_one(number):
    output = number + 1
    return output


def add_one_add_two(number_one, number_two):
    output = number_one + 1
    output += number_two + 2  # Is the same as 'output = output + number_two + 2'
    return output


Sum = add_one_add_two(1, 2)
print(Sum)

Var = 10
print(Var)

adding_one = add_one(Var)
print(adding_one)