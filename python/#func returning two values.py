#func returning two values
def func(int1,int2):
    add = int1 + int2
    multiply = int1*int2
    return add,multiply
add,multiply = (func(5,6))
print(func(add,multiply))