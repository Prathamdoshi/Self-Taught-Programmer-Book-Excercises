# chapter 5 exercise solutions
#--------------------------------------------------------------------------#

# questions 1: create a list of favorite musicians.
print('\nQuestion 1 Solution: \n')

musicians = ['Lauv','Prateek Kuhad','Rufus']

for artist in musicians:
    print(artist)

print('*'*50)
#--------------------------------------------------------------------------#

# questions 2: create a list on tuples with geo coordinates of 3 places.
print('\nQuestion 2 Solution: \n')

# list of coordinates and locations
los_angeles_coord = ('34.051922','-118.258048')
san_jose_coord = ('37.340377','-121.877689')
san_francisco_coord = ('37.793219','-122.438872')

locations = []

locations.append(los_angeles_coord)
locations.append(san_francisco_coord)
locations.append(san_jose_coord)

for location in locations:
    print(location)

print('*'*50)
#--------------------------------------------------------------------------#

# questions 3: create a dictionary that contains attributes such as heigh, fav color, fav author and etc.
print('\nQuestion 3 Solution: \n')

personal_info = {
    'name': 'Pratham Doshi',
    'height': "5'11",
    'favorite color': 'Blue',
    'fav author': 'Khaled Hussaini'
}

for key,value in personal_info.items():
    print("Key: {}, Value: {}".format(key,value))
print('*'*50)
#--------------------------------------------------------------------------#

# questions 4: 
print('\nQuestion 4 Solution: \n')

print('Hello User! Please choose from below about the information that you would like to know?')
menu_item= {
    1: 'Name',
    2: 'Height',
    3: 'Favorite Color',
    4: 'Fav author'
}

# menu print handler
for key,value in menu_item.items():
    print("Option #{} : {}".format(key,value))

user_option = int(input("Please enter the option number: "))

if user_option <=4: 
    # using the user entered option number we access the value from menu item, then it gets decrepted to lower to access answers from personal info
    print("You chose: {}, Answer : {}".format(menu_item[user_option], personal_info[menu_item[user_option].lower()]))
else:
    print('Invalid option choice')

print('*'*50)
#--------------------------------------------------------------------------#

# questions 5: create a dictionary  mapping your favorite musicians with some of songs
print('\nQuestion 5 Solution: \n')

favorite_aritsts = {}

favorite_songs = [['I like me better','Story Never Ends'],['1000 words', 'Dil Beparvah'],['Underwater','Treat you better']]

for i in range(len(musicians)):
    favorite_aritsts[musicians[i]] = favorite_songs[i]

for key,value in favorite_aritsts.items():
    print("Artist: {}, Songs: {}".format(key,value))

print('*'*50)
#--------------------------------------------------------------------------#

# questions 6: What are sets? When do you use them?
print('\nQuestion 6 Solution: \n')
print("Sets are containers that only hold original value. They are in unspecific order, immutable, unique.")
print('*'*50)
#--------------------------------------------------------------------------#