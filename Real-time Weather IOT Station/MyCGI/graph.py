import serial
import MySQLdb
from datetime import datetime

import mysql.connector
import matplotlib.pyplot as plt
tempA = []
airpA = []
waterlA = []
humA = []
windspA = []
secsA = []
xs =[]
ys = []
xs2 =[]
ys2 = []
xs3 =[]
ys3 = []
xs4 =[]
ys4 = []
xs5 =[]
ys5 = []

xxx = 0
while xxx == 0:
       date = datetime.now()
       date = date.strftime("%Y/%m/%d %H:%M:%S")
       mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="rheejantalo",
       database="appdev"
       )
       mycursor = mydb.cursor()
       mycursor.execute("Select * from weatherdata;")
       myresult = mycursor.fetchall()

       
       data = list(myresult[-1])
       print(f"data: {data}")
       print(float(data[4]))
       tempA.append(float(data[4]))
       airpA.append(float(data[1]))
       waterlA.append(float(data[2]))
       humA.append(float(data[3]))
       windspA.append(float(data[0]))
       sec = str(date)[-2:]
       secsA.append(int(sec))
    
       #graph for temp ------
       if secsA[-1] <= 1:
              ys=[]
              xs=[]
              xs.append(secsA[-1])
              ys.append(tempA[-1])
       elif secsA[-1] > 1:
              ys.append(tempA[-1])
              xs.append(secsA[-1])
       fig = plt.figure()
       axl = fig.add_subplot(1,1,1)
       axl.plot(xs, ys, 'b-', label='Growth')
       plt.title("Temp graph")
       plt.ylabel("Celcius", fontweight='bold')
       plt.xlabel(f"{date}", fontweight='bold')
       plt.axis([0,60,0,100]) #mali pani
       plt.axhspan(27,35, facecolor="green", alpha = .5) #alpha is transparency
       plt.axhspan(35,41, facecolor="yellow", alpha = 0.5)
       plt.axhspan(41,55, facecolor="orange", alpha = 0.5)
       plt.axhspan(55,100, facecolor="pink", alpha = 0.5)
       #plt.text(-5, 60, 'Here we go')
       plt.legend()
       plt.savefig('temp.png')
       #plt.show()
   
       #graph for windspeed ------
       if secsA[-1] <= 1:
              ys2=[]
              xs2=[]
              xs2.append(secsA[-1])
              ys2.append(windspA[-1])
       elif secsA[-1] > 1:
              ys2.append(windspA[-1])
              xs2.append(secsA[-1])
       fig = plt.figure()
       axl = fig.add_subplot(1,1,1)
       
       axl.plot(xs2, ys2, 'b-', label='Growth')
       plt.title("Windspeed graph")
       plt.ylabel("Knots", fontweight='bold')
       plt.xlabel(f"{date}", fontweight='bold')
       plt.axis([0,60,50,1000]) #mali pani
       plt.axhspan(270,350, facecolor="green", alpha = .5) #alpha is transparency
       plt.axhspan(350,410, facecolor="yellow", alpha = 0.5)
       plt.axhspan(410,550, facecolor="orange", alpha = 0.5)
       plt.axhspan(550,1000, facecolor="pink", alpha = 0.5)
       plt.legend()
       plt.savefig('windspeed.png')
       #plt.show()
      
       #graph for waterlevel ------ waterlA.append(float(data[2]))
       if secsA[-1] <= 1:
              ys3=[]
              xs3=[]
              xs3.append(secsA[-1])
              ys3.append(waterlA[-1])
       elif secsA[-1] > 1:
              ys3.append(waterlA[-1])
              xs3.append(secsA[-1])
       fig = plt.figure()
       axl = fig.add_subplot(1,1,1)
       
       axl.plot(xs3, ys3, 'b-', label='Growth')
       plt.title("Water level graph")
       plt.ylabel("Cubic Centimeters", fontweight='bold')
       plt.xlabel(f"{date}", fontweight='bold')
       plt.axis([0,60,50,1000]) 
       plt.axhspan(0,80, facecolor="green", alpha = .5) #alpha is transparency
       plt.axhspan(81,115, facecolor="yellow", alpha = 0.5)
       plt.axhspan(116,140, facecolor="orange", alpha = 0.5)
       plt.axhspan(141,171, facecolor="pink", alpha = 0.5)
       plt.axhspan(171,1000, facecolor="red", alpha = 0.5)
       plt.legend()
       plt.savefig('waterlevel.png')
       #plt.show()
       
       #graph for humidity humA.append(float(data[3]))
       if secsA[-1] <= 1:
              ys4=[]
              xs4=[]
              xs4.append(secsA[-1])
              ys4.append(humA[-1])
       elif secsA[-1] > 1:
              ys4.append(humA[-1])
              xs4.append(secsA[-1])
       fig = plt.figure()
       axl = fig.add_subplot(1,1,1)
       
       axl.plot(xs4, ys4, 'b-', label='Growth')
       plt.title("Humidity graph")
       plt.ylabel("Relative humidity", fontweight='bold')
       plt.xlabel(f"{date}", fontweight='bold')
       plt.axis([0,60,50,1000]) 
       plt.axhspan(0,50, facecolor="green", alpha = .5) #alpha is transparency
       plt.axhspan(51,400, facecolor="yellow", alpha = 0.5)
       plt.axhspan(401,600, facecolor="orange", alpha = 0.5)
       plt.axhspan(601,800, facecolor="pink", alpha = 0.5)
       plt.axhspan(800,1000, facecolor="red", alpha = 0.5)
       plt.legend()
       plt.savefig('humidity.png')
       #plt.show()
   
       #graph for air pressure airpA.append(float(data[1]))
       if secsA[-1] <= 1:
              ys5=[]
              xs5=[]
              xs5.append(secsA[-1])
              ys5.append(airpA[-1])
       elif secsA[-1] > 1:
              ys5.append(airpA[-1])
              xs5.append(secsA[-1])
       fig = plt.figure()
       axl = fig.add_subplot(1,1,1)
       
       axl.plot(xs5, ys5, 'b-', label='Growth')
       plt.title("Air Pressure graph")
       plt.ylabel("Millibars", fontweight='bold')
       plt.xlabel(f"{date}", fontweight='bold')
       plt.axis([0,60,50,1000]) 
       plt.axhspan(0,500, facecolor="green", alpha = .5) #alpha is transparency
       plt.axhspan(501,600, facecolor="yellow", alpha = 0.5)
       plt.axhspan(601,1000, facecolor="orange", alpha = 0.5)
       plt.legend()
       plt.savefig('airpressure.png')
       #plt.show()

