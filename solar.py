# Code to get the fossil fuel consumption trend for the states with the most GHI

import sqlite3
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np

to_db = "dataopen.db"
con = sqlite3.connect(to_db)
cur = con.cursor()
c = cur.execute("select year, month, state, sum(consumption) from fossil_fuel_consumption  where energy_source = 'Petroleum' and state in ('AZ', 'NV', 'CA', 'TX', 'FL', 'OK', 'LA', 'MS', 'AL', 'UT')  group by year, month, state order by state, year, month asc;")
#print(c.fetchall())
l = c.fetchall()
con.close()

states ={u'AZ': [[],[]], u'NV': [[],[]], u'CA': [[],[]], u'TX': [[],[]], u'FL': [[],[]], u'OK': [[],[]], u'LA' :[[],[]] , u'MS' : [[],[]], u'AL' : [[],[]], u'UT' : [[],[]]}
for item in l:
	states[item[2]][1].append(item[3])
	if item[1] <10:
		states[item[2]][0].append(int(str(item[0])+"0"+str(item[1])))
	else:
		states[item[2]][0].append(int(str(item[0])+str(item[1])))

regr = linear_model.LinearRegression()

fig = plt.figure()
for key in states:
	model = regr.fit(np.array(states[key][0]).reshape(-1,1), np.array(states[key][1]))

	plt.plot(np.array(states[key][0]).reshape(-1,1), model.predict(np.array(states[key][0]).reshape(-1,1))).

	#plt.plot(np.array(states[key][0]).reshape(-1,1), model.predict(np.array(states[key][0]).reshape(-1,1)))

plt.xlabel('Timeline')
plt.ylabel('Fossil Fuel consumption')
plt.title('Trend of fossil fuel consumption over time')

plt.show()