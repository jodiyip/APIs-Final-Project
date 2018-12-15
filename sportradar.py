import http.client
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import sqlite3
import xml.etree.ElementTree as ET
import matplotlib
import matplotlib.pyplot as plt

url = "http://api.sportradar.us/nfl-ot1/games/02b13817-bfd1-4e61-820a-55f9d8e4d36e/roster.xml?api_key=fea6p82a8ym7ccgvw3dcq2gw"
data = ssl.create_default_context()
data.check_hostname = False
data.verify_mode = ssl.CERT_NONE

html = urlopen(url, context=data).read()
soup = BeautifulSoup(html, 'html.parser')

def getPlayerData(soup):
	player_info = []
	player = soup.find_all('player')
	for x in player:
		name = x.get('name')
		height = x.get('height')
		weight = x.get('weight')
		position = x.get('position')
		player_tup = (name, height, weight, position)
		player_info.append(player_tup)
	# print(player_info)
	return(player_info)

def rangeOfWeight(soup):
	data = getPlayerData(soup)
	r175200 = 0
	r200225 = 0
	r225250 = 0
	r250275 = 0
	r275300 = 0
	r300325 = 0
	r325350 = 0
	for x in data:
		weight = float(x[2])
		if weight >= 175 and weight < 200:
			r175200 += 1
		elif weight >= 200 and weight < 225:
			r200225 += 1
		elif weight >= 225 and weight < 250:
			r225250 += 1
		elif weight >= 250 and weight < 275:
			r250275 += 1
		elif weight >= 275 and weight < 300:
			r250275 += 1
		elif weight >= 300 and weight < 325:
			r300325 += 1
		elif weight >= 325 and weight < 350:
			r325350 += 1
	# lst = ['r175200', 'r200225', 'r225250', 'r250275', 'r275300', 'r300325', 'r325350']
	dictionary = dict()
	dictionary["175-199"] = r175200
	dictionary["200-224"] = r200225
	dictionary["225-249"] = r225250
	dictionary["250-274"] = r250275
	dictionary["275-299"] = r275300
	dictionary["300-324"] = r300325
	dictionary["325-349"] = r325350
	return (dictionary)

def removeDuplicate(dup):
	lst = list()
	for x in dup:
		if x not in lst:
			lst.append(x)
	return (lst)

def listOfPositions(soup):
	data = getPlayerData(soup)
	lst_position = list()
	for x in data:
		position = str(x[3])
		lst_position.append(position)
	new_list = list()
	# list of all positions
	new_list = removeDuplicate(lst_position)
	return(new_list)

def averageHeightforPosition(soup):
	data = getPlayerData(soup)
	new_list = listOfPositions(soup)
	position0 = position1 = position2 = position3 = position4 = position5 = position6 = position7 = position8 = position9 = position10 = position11 = position12 = position13 = position14 = position15 = position16 = position17 = position18 = position19 = 0
	count0 = count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = count10 = count11 = count12 = count13 = count14 = count15 = count16 = count17 = count18 = count19 = 0
	average0 = average1 = average2 = average3 = average4 = average5 = average6 = average7 = average8 = average9 = average10 = average11 = average12 = average13 = average14 = average15 = average16 = average17 = average18 = average19 = 0
	# name, height, weight, position
	for y in data:
		# y[3] = position
		if(new_list[0] == y[3]):
			position0 += float(y[1])
			count0+=1
		elif(new_list[1] == y[3]):
			position1 += float(y[1])
			count1+=1
		elif(new_list[2] == y[3]):
			position2 += float(y[1])
			count2+=1
		elif(new_list[3] == y[3]):
			position3 += float(y[1])
			count3+=1
		elif(new_list[4] == y[3]):
			position4 += float(y[1])
			count4+=1
		elif(new_list[5] == y[3]):
			position5 += float(y[1])
			count5+=1
		elif(new_list[6] == y[3]):
			position6 += float(y[1])
			count6+=1
		elif(new_list[7] == y[3]):
			position7 += float(y[1])
			count7+=1
		elif(new_list[8] == y[3]):
			position8 += float(y[1])
			count8+=1
		elif(new_list[9] == y[3]):
			position9 += float(y[1])
			count9+=1
		elif(new_list[10] == y[3]):
			position10 += float(y[1])
			count10+=1
		elif(new_list[11] == y[3]):
			position11 += float(y[1])
			count11+=1
		elif(new_list[12] == y[3]):
			position12 += float(y[1])
			count12+=1
		elif(new_list[13] == y[3]):
			position13 += float(y[1])
			count13+=1
		elif(new_list[14] == y[3]):
			position14 += float(y[1])
			count14+=1
		elif(new_list[15] == y[3]):
			position15 += float(y[1])
			count15+=1
		elif(new_list[16] == y[3]):
			position16 += float(y[1])
			count16+=1
		elif(new_list[17] == y[3]):
			position17 += float(y[1])
			count17+=1
		elif(new_list[18] == y[3]):
			position18 += float(y[1])
			count18+=1
		elif(new_list[19] == y[3]):
			position19 += float(y[1])
			count19+=1
	average0 = position0 / count0
	average1 = position1 / count1
	average2 = position2 / count2
	average3 = position3 / count3
	average4 = position4 / count4
	average5 = position5 / count5
	average6 = position6 / count6
	average7 = position7 / count7
	average8 = position8 / count8
	average9 = position9 / count9
	average10 = position10 / count10
	average11 = position11 / count11
	average12 = position12/ count12
	average13 = position13 / count13
	average14 = position14 / count14
	average15 = position15 / count15
	average16 = position16 / count16
	average17 = position17/ count17
	average18 = position18 / count18
	average19 = position19 / count19
	average = [average0, average1, average2, average3, average4, average5, average6, average7, average8, average9, average10, average11, average12, average13, average14, average15, average16, average17, average18, average19]
	dictionary = dict()
	dictionary["DL"] = average0
	dictionary["QB"] = average1
	dictionary["OL"] = average2
	dictionary["LB"] = average3
	dictionary["WR"] = average4
	dictionary["TE"] = average5
	dictionary["RB"] = average6
	dictionary["DE"] = average7
	dictionary["DT"] = average8
	dictionary["DB"] = average9
	dictionary["C"] = average10
	dictionary["K"] = average11
	dictionary["FB"] = average12
	dictionary["T"] = average13
	dictionary["SS"] = average14
	dictionary["B"] = average15
	dictionary["P"] = average16
	dictionary["LS"] = average17
	dictionary["G"] = average18
	dictionary["OLB"] = average19
	# print(dictionary)
	return(dictionary)
averageHeightforPosition(soup)

conn = sqlite3.connect('sportradar.sqlite')
cur = conn.cursor()

def createTableofData(soup, conn, cur):
	cur.execute('CREATE TABLE IF NOT EXISTS PlayerSize (name TEXT, height INTEGER, weight INTEGER, position TEXT)')
	soup = getPlayerData(soup)
	for player in soup:
		_name = player[0]
		_height = player[1]
		_weight = player[2]
		_position = player[3]
		cur.execute('INSERT INTO PlayerSize (name, height, weight, position) VALUES (?, ?, ?, ?)',
		 (_name, _height, _weight, _position))
		conn.commit()
createTableofData(soup, conn, cur)

def createBarGraphofWeights(soup):
	# fig, ax = plt.subplots()
	xValues = rangeOfWeight(soup).keys()
	yValues = rangeOfWeight(soup).values()
	plt.bar(xValues, yValues, color=(0.5, 0.1, 0.7, 0.6))
	plt.xlabel('weight range (pounds)')
	plt.ylabel('number of players')
	plt.title('Seattle Seahawks And New England Patriots Weight Distribution')
	plt.show()

def createBarGraphOfAvgHeight(soup):
	# list of all positions
	xValues = averageHeightforPosition(soup).keys()
	yValues = averageHeightforPosition(soup).values()
	plt.bar(xValues, yValues, color=(0.8, 0.5, 0.2, 0.6))
	plt.xlabel('positions')
	plt.ylabel('height (inches)')
	plt.title('Seattle Seahawks And New England Patriots Average Height Based On Position')
	plt.show()
	plt.legend([])
createBarGraphOfAvgHeight(soup)
