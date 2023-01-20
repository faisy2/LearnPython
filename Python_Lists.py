#Storing Row Elements into Variables
track_name_row_2="Instagram"
price_row_2=0.0
rating_count_tot_row_2=2161558

#Storing Rows as Lists
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_1)
print(type(row_1))
row_2=['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3=['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
#List Length
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
empty_row = []
row_2_length=len(row_2)
empty_row_length=len(empty_row)
#List Indexing
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

track_name_index=row_2.index('Instagram')
user_rating_index=row_3.index(4.5)
#Retrieving Values from Lists
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
ratings_1=row_1[3]
ratings_2=row_2[3]
ratings_3=row_3[3]
total=ratings_1+ratings_2+ratings_3
average=total/3
# Negative Indexing
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
rating_1=row_1[-1]
rating_2=row_2[-1]
rating_3=row_3[-1]
total_rating=rating_1+rating_2+rating_3
average_rating=total_rating/3
#Retrieving Multiple List Elements
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]
fb_rating_data=[row_1[0],row_1[3],row_1[-1]]
insta_rating_data=[row_2[0],row_2[3],row_2[-1]]
minecraft_rating_data=[row_5[0],row_5[3],row_5[-1]]
total_rating=fb_rating_data[2]+insta_rating_data[2]+minecraft_rating_data[2]
average_rating=total_rating/3
#List Slicing
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012,4.5]
last_3_fb=row_1[-3:]
minecraft_3_4=row_5[2:4]
print(last_3_fb)
print(minecraft_3_4)
#List of Lists

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]
games_apps=[row_3,row_4,row_5]