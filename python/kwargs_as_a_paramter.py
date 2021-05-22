#*kwargs_as_a_parameter
#def fun(**kwargs):#kwargs save input as a dictionary
 #   print(kwargs)
#fun(first_name='anuj',last_name='joshi')

def fun1(**kwargs):
    for k,v in kwargs.item():
        print(f"{k}:{v}")
d = {'first_name':'anuj','last_name':'joshi'}
fun1(**d)
