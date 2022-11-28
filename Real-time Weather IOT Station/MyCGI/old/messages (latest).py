def getmessage():
       import mysql.connector

       mydb = mysql.connector.connect(
              host ="localhost",
              user="root",
              password="rheejantalo",
              database="appdev"
              )
       mycursor = mydb.cursor()
       mycursor.execute("Select * from weatherdata;")
       
       myresult = mycursor.fetchall()
       messagelist = []
       data = list(myresult[-1])
       currtemp = int(data[4])
       currairpressure= int(data[1])
       currwaterlevel= int(data[2])
       currhumidity= int(data[3])
       currwindspeed= int(data[0])
       message=""
       
    
       #-----messages for temperature-----
       if currtemp <= 0:
              message = "Extremely Cold temperature, be careful for frostbite"
              messagelist.append(message)
       elif 10 > currtemp > 0  :
              message = "Extremely Cold temperature"
              messagelist.append(message)
       elif 22  > currtemp > 10  :
              message = "Very cold temperature and it could rain, please wear jackets and bring umbrella"
              messagelist.append(message)
       elif 27 > currtemp > 22  :
              message = "Could rain, bring umbrella"
              messagelist.append(message)
       elif 31 > currtemp > 28  :
              message = "Normal temperature, go have fun outside"
              messagelist.append(message)
       elif 40 > currtemp > 32  :
              message = "Hot temperature, can possibly experience heat cramps and exhaustion"
              messagelist.append(message)
       elif 52 > currtemp > 41  :
              message = "Very hot temperature, more likely to experience heat cramps, limit your activity"
              messagelist.append(message)
       elif currtemp > 52:
              message="Extremely hot temperature, could lead to heatstroke"
              messagelist.append(message)

       #-----messages for water level-----
       if currwaterlevel <= 80:
              message = "Very Low"
              messagelist.append(message)
       elif 115 > currwaterlevel > 80  :
              message = "Low"
              messagelist.append(message)
       elif 140 > currwaterlevel > 115  :
              message = "High"
              messagelist.append(message)
       elif 170 > currwaterlevel > 140  :
              message = "Very High"
              messagelist.append(message)
       elif currwaterlevel > 170:
              message="Dangerously High"
              messagelist.append(message)
       
  
       return messagelist
