#in keyword in dict
users ={
    'name' : 'anuj',
    'age' : 18,
    'fav_mov' : ['stranger things','money heist' ],
    'fav_tunes' : ['ily'],
    }
    #check if keys
if 'name' in users:
    print('present')
else:
    print('not present')
#check if values
if 18 in users.values():
    print('present')
else:
    print('not present')