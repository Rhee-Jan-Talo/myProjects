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
       plt.ylabel("Celcius", fontweight='bold')
       plt.xlabel(f"{date}", fontweight='bold')
       plt.axis([0,60,0,100]) #mali pani
       plt.axhspan(27,35, facecolor="green", alpha = .5) #alpha is transparency
       plt.axhspan(35,41, facecolor="yellow", alpha = 0.5)
       plt.axhspan(41,55, facecolor="orange", alpha = 0.5)
       plt.axhspan(55,100, facecolor="pink", alpha = 0.5)
       plt.legend()
       plt.show()
       plt.savefig('temp.png')
       
