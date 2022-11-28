import mysql.connector
import matplotlib.pyplot as plt
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
x = 0
while x == 0:
       mycursor.execute("Select * from weatherdata;")
       myresult = mycursor.fetchall()

       
       latest = myresult[-1]

       windspA.append(latest[0])
       airpA.append(latest[1])
       waterlA.append(latest[2])
       humA.append(latest[3])
       tempA.append(latest[4])
       secsA.append(latest[6])
              
       '''
       for i in myresult: # transfer data to array
              windspA.append(i[0])
              airpA.append(i[1])
              waterlA.append(i[2])
              humA.append(i[3])
              tempA.append(i[4])
              secsA.append(i[6])
       #print(str(secsA[len(secsA)-1])[-2:])
       '''      

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
       plt.axis([10,60,10,100]) #x and y axis
       plt.axhspan(0,20, facecolor="blue", alpha = .5) #alpha is transparency
       plt.axhspan(30,40, facecolor="yellow", alpha = 0.5)
       plt.axhspan(50,60, facecolor="green", alpha = 0.5)
       plt.axhspan(70,80, facecolor="blue", alpha = 0.5)
       plt.axhspan(90,100, facecolor="yellow", alpha = 0.5)
       plt.legend()
       plt.savefig('temp.png')
       plt.show()

       



              
