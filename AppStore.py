import MySQLdb
from csv import reader

#Extracting data from a CSV file and converting it to a list

var_open = open('AppleStore.csv',encoding="utf8")
var_read = reader((var_open))
apps_list = list(var_read)
app_list_header=(apps_list[0])
apps_list = apps_list[1:]
# print(app_list_header)
# print(len(apps_list))


def App_row(index):
	for temp in apps_list:
	    print(temp[index])
		 
# 		                      PART 1: Cleaning of Data

# Removing all non English app from our source and allowing upto 3 non english char per name

english_app=[]
def english (name):
	flag =0
	for temp1 in name:
		if ord(temp1)>127:
			flag +=1
	
	if flag >3:
		return False
	else:
		return True

for temp in apps_list:
	name1 = temp[2]
	if english(name1) :
		english_app.append(temp)
# print(*english_app,sep='\n')
# print(len(english_app))

# Removing all the paid apps

free_app = []
for temp in english_app:
	price = float(temp[5])
	if price == 0.0:
		free_app.append(temp)
# print(*free_app,sep='\n')
# print(len(free_app))

#Check for any duplicate app entry
duplicate ={}
flag =0
for temp in free_app:
	app_name = temp[2]
	if app_name in duplicate:
		 duplicate[app_name] +=1
		
# print(duplicate)
# It gives output an empty set so no duplicate present


		               # PART 2 : Extracting important Facts
		               
# #Finding the frequency percent of apps in each genre
def order(index):
	table ={}
	flag = 0
	for temp in free_app:
		flag +=1
		genre = temp[index]
		if genre in table:
			table[genre] +=1
		else:
			table[genre] =1

	feq_per = {}
	for temp in table:
		percentage = (table[temp]/flag)*100
		feq_per[temp] = percentage
	return feq_per
def frequency(index):
	value = order(index)
	display = []
	for temp in value:
		temp_tuple = (value[temp],temp)
		display.append(temp_tuple)
	sorted_table = sorted(display, reverse=True)
	for temp in sorted_table:
		print(temp[1]," : ",temp[0])
# frequency(12)
	
	# Finding which app has the highest rating and is in which genre
rat_gen ={}
rat_list=[]

for temp in free_app:
	rating = float(temp[6])
	genre = temp[12]
	name = temp[2]
	if genre in rat_gen and rat_gen[genre]<rating:
		rat_gen[genre] = rating
	elif genre not in rat_gen:
		rat_gen[genre] = rating
		
# print(rat_gen)

for temp in rat_gen:      #printing in decending order
	rat_tuple = (rat_gen[temp],temp)
	rat_list.append(rat_tuple)
sort_rating = sorted(rat_list, reverse=True)
for temp in sort_rating:
 print(temp[1],' : ',temp[0])

#seeing individual social networking app with its rating
for temp in free_app:
	if temp[12] == 'Social Networking':
		print(temp[2],' : ',temp[6])
