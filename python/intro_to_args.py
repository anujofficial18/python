#intro_to_*args
#*operators
def total(a,b):
    return a+b
def all_total(*args):
    total = 0
    for num in args:
        total += num
    return total
print(all_total(1,2,3,4,5,6,7,8,9,10))

#args_with_normal_parameter
def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply
nums = (2,3,4)
print(multiply_nums(*nums))  # to unpack value use "*" with variable like *nums 