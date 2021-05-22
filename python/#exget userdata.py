#exget userdata
user = {
   # 'name' : 'anuj',
  #  'age' : 18,
 #   'fav_mov' : ['stranger things','money heist' ],
#    'fav_tunes' : ['ily'],
}
name = input('what is your name')
age = input('what is your age')
fav_mov = input('what is your fav mov').split(',')
fav_song = input('what is your fav song').split(',')

user['name'] = name
user['age'] = age
user['fav_mov'] = fav_mov
user['fav_song'] = fav_song

for key, value in user.items():
    print(f"{key} : {value}")