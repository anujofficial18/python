#ex_args
def power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        "no args"
nums = [1,2,3]
print(power(3,*nums))