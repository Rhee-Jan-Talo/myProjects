import mysql.connector
import matplotlib.pyplot as plt

print("Content-Type: text/html\n")

tempA = []
airpA = []
waterlA = []
humA = []
windspA = []
secsA = []
mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="rheejantalo",
       database="appdev"
       )

mycursor = mydb.cursor()

mycursor.execute("Select * from weatherdata;")
myresult = mycursor.fetchall()

for i in myresult: # transfer data to array
       windspA.append(i[0])
       airpA.append(i[1])
       waterlA.append(i[2])
       humA.append(i[3])
       tempA.append(i[4])
       secsA.append(i[6])
#print(str(secsA[len(secsA)-1])[-2:])

#----- making of graph (TEMP) -----
xs =[]
ys = []
for i in tempA:
       ys.append(i)
for  i in secsA:
       a = str(i)[-2:]
       xs.append(int(a))  
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.clear()
axl.plot(xs, ys, 'b--', label='abc')
plt.title("Temp graph")
plt.ylabel("Y Axis", fontweight='bold')
plt.xlabel("X Axis", fontweight='bold')
plt.axis([10,60,10,100]) #mali pani
plt.axhspan(0,20, facecolor="blue", alpha = .5) #alpha is transparency
plt.axhspan(30,40, facecolor="yellow", alpha = 0.5)
plt.axhspan(50,60, facecolor="green", alpha = 0.5)
plt.axhspan(70,80, facecolor="blue", alpha = 0.5)
plt.axhspan(90,100, facecolor="yellow", alpha = 0.5)
plt.legend()
plt.savefig('temp.png')
plt.show()

#----- making of graph (WINDSPEED) -----

xs2 =[]
ys2 = []
for i in windspA:
       ys2.append(i)
for  i in secsA:
       a = str(i)[-2:]
       xs2.append(int(a))
       
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.clear()
axl.plot(xs2, ys2, 'b--', label='abcd')
plt.title("Windspeed graph")
plt.ylabel("Y Axis", fontweight='bold')
plt.xlabel("X Axis", fontweight='bold')
plt.axis([1,1000,1,1000]) #mali pani
plt.axhspan(100,200, facecolor="blue", alpha = .5) #alpha is transparency
plt.axhspan(300,400, facecolor="yellow", alpha = 0.5)
plt.axhspan(500,600, facecolor="green", alpha = 0.5)
plt.axhspan(700,800, facecolor="blue", alpha = 0.5)
plt.axhspan(900,1000, facecolor="yellow", alpha = 0.5)
plt.legend()
plt.savefig('winds.png')
plt.show()

#----- making of graph (AIR PRESSURE) -----

xs =[]
ys = []
for i in airpA:
       ys.append(i)
for  i in secsA:
       a = str(i)[-2:]
       xs.append(a)  
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.clear()
axl.plot(xs, ys, 'b--', label='abc')
plt.title("Air Pressure graph")
plt.ylabel("Y Axis", fontweight='bold')
plt.xlabel("X Axis", fontweight='bold')
plt.axis([1,1000,1,1000]) #mali pani
plt.axhspan(100,200, facecolor="blue", alpha = .5) #alpha is transparency
plt.axhspan(300,400, facecolor="yellow", alpha = 0.5)
plt.axhspan(500,600, facecolor="green", alpha = 0.5)
plt.axhspan(700,800, facecolor="blue", alpha = 0.5)
plt.axhspan(900,1000, facecolor="yellow", alpha = 0.5)
plt.legend()
plt.savefig('airP.png')
plt.show()

#----- making of graph (HUMIDITY) -----

xs =[]
ys = []
for i in humA:
       ys.append(i)
for  i in secsA:
       a = str(i)[-2:]
       xs.append(a)  
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.clear()
axl.plot(xs, ys, 'b--', label='abc')
plt.title("Humidity graph")
plt.ylabel("Y Axis", fontweight='bold')
plt.xlabel("X Axis", fontweight='bold')
plt.axis([1,1000,1,1000]) #mali pani
plt.axhspan(100,200, facecolor="blue", alpha = .5) #alpha is transparency
plt.axhspan(300,400, facecolor="yellow", alpha = 0.5)
plt.axhspan(500,600, facecolor="green", alpha = 0.5)
plt.axhspan(700,800, facecolor="blue", alpha = 0.5)
plt.axhspan(900,1000, facecolor="yellow", alpha = 0.5)
plt.legend()
plt.savefig('hum.png')
plt.show()

#----- making of graph (WATER LEVEL) -----

for i in waterlA:
       ys.append(i)
for  i in secsA:
       a = str(i)[-2:]
       xs.append(a)  
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.clear()
axl.plot(xs, ys, 'b--', label='abc')
plt.title("Water Level graph")
plt.ylabel("Y Axis", fontweight='bold')
plt.xlabel("X Axis", fontweight='bold')
plt.axis([1,1000,1,1000]) #mali pani
plt.axhspan(100,200, facecolor="blue", alpha = .5) #alpha is transparency
plt.axhspan(300,400, facecolor="yellow", alpha = 0.5)
plt.axhspan(500,600, facecolor="green", alpha = 0.5)
plt.axhspan(700,800, facecolor="blue", alpha = 0.5)
plt.axhspan(900,1000, facecolor="yellow", alpha = 0.5)
plt.legend()
plt.savefig('water.png')
plt.show()
       



              
