import serial
import MySQLdb
from datetime import datetime

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
                print (e)
