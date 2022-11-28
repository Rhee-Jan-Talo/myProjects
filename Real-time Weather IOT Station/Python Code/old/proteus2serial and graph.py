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

dbConn = MySQLdb.connect("localhost","root","rheejantalo","appdev") or die ("error could not connect")

try:
         print("Connecting....")
         arduino = serial.Serial(port='COM2', baudrate=9600)
except:
         print("Failed to connect")
else:
         print("successfully connected")
         
while 1:
       try:
              arduinodata = arduino.readline() #read the data from arduino
              sensorsdata = arduinodata.decode("utf-8") #convert the data into string
              print(sensorsdata)
              try:
                     date = datetime.now()
                     date = date.strftime("%Y/%m/%d %H:%M:%S")
                     print(date)
                     a_list = sensorsdata.split()
                     cursor = dbConn.cursor()
                     query = "INSERT INTO weatherdata (tc, wl, hu, ap, ws, tf, dtime) VALUES ('"+a_list[0]+"','"+a_list[1]+"','"+a_list[2]+"','"+a_list[3]+"','"+a_list[4]+"','"+a_list[5]+ "','" +date+"');"
                     cursor.execute(query)
                     dbConn.commit()
                     cursor.close()
              except MySQLdb.IntegrityError:
                     print("Failed to insert data")
              finally:
                     cursor.close()
       except Exception as e:
                print(e)
       #------------------------------------------
       mydb = mysql.connector.connect(
       host ="localhost",
       user="root",
       password="rheejantalo",
       database="appdev"
       )
       
       mycursor = mydb.cursor()
       mycursor.execute("Select * from weatherdata;")
       myresult = mycursor.fetchall()

       data = sensorsdata.split(" ")
       temp = data[0]
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
       plt.show()
       plt.close()

       

       

       

       



