import cgi, cgitb
import matplotlib.pyplot as plt
import mysql.connector
#loop for date----
form = cgi.FieldStorage()
dfrom = str(form.getvalue("date1"))
d = dfrom.split('-')
dfrom =""
for i in d:
      dfrom = dfrom + i +"/"
tfrom = str(form.getvalue("date2"))
t = tfrom.split('-')
tfrom =""
for i in t:
       tfrom = tfrom + i +"/"
#loop for date----

       
dfrom = dfrom[:-1]
tfrom = tfrom[:-1]
xs =[]
ys = []
tr = []
tr2 = []
ys2 = [] #windspeed
ys3 = [] #waterlevel
ys4 = [] #humidity
ys5 = [] #airpressure

mydb = mysql.connector.connect(
host ="localhost",
user="root",
password="rheejantalo",
database="appdev"
              )
mycursor = mydb.cursor()
query= f"select * from weatherdata where dtime between '{dfrom}' and '{tfrom}' "
query2 = f"select dtime, AVG(tc), AVG(ws), AVG(wl), AVG(hu), AVG(ap) from weatherdata where dtime >= '{dfrom}' and dtime <= '{tfrom}' group by date(dtime)"
mycursor.execute(query2)
myresult = mycursor.fetchall()



teststr = ""
for i in myresult:
      ys.append(float(i[1]))
      ys2.append(float(i[2])) 
      ys3.append(float(i[3]))
      ys4.append(float(i[4]))
      ys5.append(float(i[5]))
      teststr=i[0].strftime("%Y/%m/%d")
      xs.append(teststr)


#average temp
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(xs, ys, 'b-', label='Growth')
plt.title("Temperature graph (average)")
plt.ylabel("Average Temperature", fontweight='bold')
plt.xlabel("Days", fontweight='bold')
plt.axhspan(27,35, facecolor="green", alpha = .5) #alpha is transparency
plt.axhspan(35,41, facecolor="yellow", alpha = 0.5)
plt.axhspan(41,55, facecolor="orange", alpha = 0.5)
plt.axhspan(55,100, facecolor="pink", alpha = 0.5)
plt.legend()
plt.savefig('tempave.png')

#average wind speed
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(xs, ys2, 'b-', label='Growth')
plt.title("Winds Speed graph (average)")
plt.ylabel("Average Windspeed", fontweight='bold')
plt.xlabel("Days", fontweight='bold')
plt.axhspan(270,350, facecolor="green", alpha = .5) #alpha is transparency
plt.axhspan(350,410, facecolor="yellow", alpha = 0.5)
plt.axhspan(410,550, facecolor="orange", alpha = 0.5)
plt.axhspan(550,1000, facecolor="pink", alpha = 0.5)
plt.legend()
plt.savefig('windsave.png')

#average waterlevel
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(xs, ys3, 'b-', label='Growth')
plt.title("Water Level graph (average)")
plt.ylabel("Average Water Level", fontweight='bold')
plt.xlabel("Days", fontweight='bold')
plt.axhspan(81,115, facecolor="yellow", alpha = 0.5)
plt.axhspan(116,140, facecolor="orange", alpha = 0.5)
plt.axhspan(141,171, facecolor="pink", alpha = 0.5)
plt.axhspan(171,1000, facecolor="red", alpha = 0.5)
plt.legend()
plt.savefig('waterave.png')

#average humidity
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(xs, ys4, 'b-', label='Growth')
plt.title("Humidity graph (average)")
plt.ylabel("Average Humidity", fontweight='bold')
plt.xlabel("Days", fontweight='bold')
plt.axhspan(0,50, facecolor="green", alpha = .5) #alpha is transparency
plt.axhspan(51,400, facecolor="yellow", alpha = 0.5)
plt.axhspan(401,600, facecolor="orange", alpha = 0.5)
plt.axhspan(601,800, facecolor="pink", alpha = 0.5)
plt.axhspan(800,1000, facecolor="red", alpha = 0.5)
plt.legend()
plt.savefig('humave.png')

#average air pressure
fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(xs, ys5, 'b-', label='Growth')
plt.title("Air Pressure graph (average)")
plt.ylabel("Average Temperature", fontweight='bold')
plt.xlabel("Days", fontweight='bold')
plt.axhspan(0,500, facecolor="green", alpha = .5) #alpha is transparency
plt.axhspan(501,600, facecolor="yellow", alpha = 0.5)
plt.axhspan(601,1000, facecolor="orange", alpha = 0.5)
plt.legend()
plt.savefig('airpave.png')






print("Content-Type: text/html\n")
a="""
<head>
</head>
<body>


<form method="POST" action="menu.py">
<button type ="submit"
style="height:35px; width:200px; color: black; font-size:16px; border-radius: 10px; ">
Back to Main Menu</button>
</form>



     """
#b = f"<center><h1> {myresult} </h1>" # From: {dfrom} To: {tfrom} QUERY: '{query}'</h1><h1>{myresult}
c = """
<table>
              <thead>
                     <tr>
                            <th><h2>Calculated Average of Graphs</h2></th>
                            <th><img src="tempave.png" alt="loading please wait..."></th>
                            <th><img src="windsave.png" alt="loading please wait..."></th>   
                     </tr>
              </thead>
              <tbody>
                     <tr>
                            <th><img src="waterave.png" alt="loading please wait..."></th>
                            <th><img src="humave.png" alt="loading please wait..."></th>
                            <th><img src="airpave.png" alt="loading please wait..."></th>
                            
                     </tr>
              </tbody>
       </table>


       

</body>
       """
print(a + c) #+ b

