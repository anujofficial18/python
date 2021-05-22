#kwargs_2
#def fun(name = '',age = '18'):
#   print(name)
#  print(age)
#fun('anuj')

#normal parameter
def func(name,*args,last_name= 'unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('anuj',1,2,3,a=1,b=2)