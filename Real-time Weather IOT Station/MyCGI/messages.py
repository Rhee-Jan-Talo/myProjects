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
              message = "Caution: Extremely Cold temperature, be careful for frostbite"
              messagelist.append(message)
       elif 10 > currtemp > 1  :
              message = "Caution: Extremely Cold temperature"
              messagelist.append(message)
       elif 22  > currtemp > 11  :
              message = "Caution: Very cold temperature and it could rain, please wear jackets and bring umbrella"
              messagelist.append(message)
       elif 27 > currtemp > 23  :
              message = "Caution: Could rain, bring umbrella"
              messagelist.append(message)
       elif 31 > currtemp > 28  :
              message = "Caution: Normal temperature, go have fun outside"
              messagelist.append(message)
       elif 40 > currtemp > 32  :
              message = "Caution: Hot temperature, can possibly experience heat cramps and exhaustion"
              messagelist.append(message)
       elif 52 > currtemp > 41  :
              message = "Caution: Very hot temperature, more likely to experience heat cramps, limit your activity"
              messagelist.append(message)
       elif currtemp >= 53:
              message="Caution: Extremely hot temperature, could lead to heatstroke"
              messagelist.append(message)

       #-----messages for water level-----
       if currwaterlevel <= 80:
              message = "Warning: Very Low Water level"
              messagelist.append(message)
       elif 115 > currwaterlevel > 81  :
              message = "Warning: Low Water level"
              messagelist.append(message)
       elif 140 > currwaterlevel > 116  :
              message = "Warning: High Water Level, stay at your homes and wait for evacuation procedures"
              messagelist.append(message)
       elif 170 > currwaterlevel > 141  :
              message = "Warning: Very High Water Level, slowly evacuate people and prioritize olderly and kids"
              messagelist.append(message)
       elif currwaterlevel > 171:
              message="Warning: Dangerously High water level, people should already be evacuated in their homes."
              messagelist.append(message)

       #-----messages for Wind speed-----       
       if currwindspeed <= 200:
              message = "Caution: Normal Wind Speed"
              messagelist.append(message)
       elif 330 > currwindspeed > 201  :
              message = "Caution: Strong Wind Speed"
              messagelist.append(message)
       elif 470 > currwindspeed > 331  :
              message = "Caution: High Wind Speed"
              messagelist.append(message)
       elif 630 > currwindspeed > 471  :
              message = "Caution: Very High Wind Speed"
              messagelist.append(message)
       elif currwindspeed > 631:
              message="Caution: Dangerously High Wind Speed"
              messagelist.append(message)

       #-----messages for air pressure-----
       if currairpressure <= 500:
              message = "Caution: Low Air Pressure"
              messagelist.append(message)
       elif 501 < currairpressure < 600  :
              message = "Caution: Average Air Pressure"
              messagelist.append(message)
       elif currairpressure >= 601  :
              message = "Caution: High Air Pressure"
              messagelist.append(message)
      

       #-----messages for Humidity-----
       if currhumidity <= 50:
              message = "Caution: Extremely Low Humidity"
              messagelist.append(message)
       elif 51 < currhumidity < 400 :
              message = "Caution: Low Humidity"
              messagelist.append(message)
       elif 401 < currhumidity < 600  :
              message = "Caution: Normal Humidity"
              messagelist.append(message)
       elif 601 < currhumidity < 800  :
              message = "Caution: High Humidity"
              messagelist.append(message)
       elif currhumidity >= 801:
              message="Caution: Extremely High Humidity"
              messagelist.append(message)


       return messagelist


