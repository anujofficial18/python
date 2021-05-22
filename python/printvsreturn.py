#printvsreturn
def add_three(a,b,c):
    print(a+b+c)
add_three(5,5,5) 
#practice
def last_char(name):
    return name[-1]
print(last_char("anuj joshi"))

def odd_even(number):
    if number%2 ==0:
        return "even"
    return "odd"
print(odd_even(10))
#
def odd_even(num):
    return num%2 == 0 
print(odd_even(9))  #if even no. "true"  if odd, "false"