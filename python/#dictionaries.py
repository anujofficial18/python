#dictionaries
user = {'name':'anuj','age':'18'}#for dictionaries '{}'are used
print(user)

#method2
#dict method
user1 = dict(name ='anuj',age = '18')
print(user1)

#how to access data from dictionaries
print(user['name'])
print(user['age'])

#data which dict. can store ,,numbers,string,list,dictionaries
user_info = {
    'name' : 'anuj',
    'age' : 18,
    'fav_mov' : ['stranger things','money heist' ],
    'fav_tunes' : ['ily'],
}
print(user_info)
print(user_info['fav_mov'])


users ={
    'user1' :{
    'name' : 'anuj',
    'age' : 18,
    'fav_mov' : ['stranger things','money heist' ],
    'fav_tunes' : ['ily'],
    },
    'user2' :{
    'name' : 'mayank',
    'age' : 19,
    'fav_mov' : ['jagga jasoos','money heist' ],
    'fav_tunes' : ['matargasti'],
    }
}
print(users['user1'])