#looping in dict
user ={
    'name' : 'anuj',
    'age' : 18,
    'fav_mov' : ['stranger things','money heist' ],
    'fav_tunes' : ['ily'],
    }
for i in user:    #for values [for i in users.value():]
    print(i)
#valuemethod
user_values = user.values()  #for keys replace values ---->keys
print(user_values)

#item method
#user_items = user.items()
#print(user.items) 
for i ,j in user.items():
    print(f"key is {i} and value is {j}")