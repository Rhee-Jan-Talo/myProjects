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
       temp = data[4]
       tempA.append(float(temp))
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
       
       axl.plot(xs, ys, 'b-', label='abc')
       plt.title("Temp graph")
       plt.ylabel("Y Axis", fontweight='bold')
       plt.xlabel("X Axis", fontweight='bold')
       plt.axis([1,60,1,100]) #mali pani
       plt.axhspan(0,20, facecolor="blue", alpha = .5) #alpha is transparency
       plt.axhspan(30,40, facecolor="yellow", alpha = 0.5)
       plt.axhspan(50,60, facecolor="green", alpha = 0.5)
       plt.axhspan(70,80, facecolor="blue", alpha = 0.5)
       plt.axhspan(90,100, facecolor="yellow", alpha = 0.5)
       plt.legend()
       plt.savefig('temp.png')
       
