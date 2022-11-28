import messages
from datetime import datetime

message = ""
message = messages.getmessage()
messageTemp = str(message[0])
messageAirp = str(message[3])
messageWL = str(message[1])
messageHum = str(message[4])

messageWS = str(message[2])
date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

print("Content-Type: text/html\n")
b = f" Temp: {messageTemp}  \n AirP: {messageAirp} \n WL: {messageWL} \n HUM: {messageHum} \n WS: {messageWS}"
a=   """
       <head>
       <title>
        Weather Station IOT by Rhee Pogi
       </title>
       </head>
       <meta http-equiv="refresh" content=".1">
       <style>
       ul {white-space: nowrap;}
       ul, li {list-style: none;display: inline; margin-bottom: 100px; margin-top: 90px;}
       </style>
       <body>
       
       <center>
       <table>
       
       <thead>
       <tr>
       
       <th>
       <p><h2>WELCOME TO WEATHER IOT STATION LIVE BROADCAST<h2></p>
       <p>
       <form method="POST" action="menu.py">
       <button type ="submit"
              style="height:35px; width:200px; color: black; font-size:16px; border-radius: 10px; ">
              Back to Main Menu</button>
       </form>
       </p>


       </th>
       <th><img src="temp.png" alt="loading please wait...">
       <center style="color: red; font-family:calibri ;font-size:23px;">
       """
mess1=f"{messageTemp}"  
b = """
       </center></th>
       <th><img src="humidity.png" alt="loading please wait...">
       <center style="color: red; font-family:calibri ;font-size:23px;">
       """
mess2=f"{messageHum}"  
c = """
       </center>
       </th>   
       </tr>
       </thead>
       <tbody>
       <tr>
       <th><img src="waterlevel.png" alt="loading please wait...">
       <center style="color: red; font-family:calibri ;font-size:23px;">
       """
mess3=f"{messageWL}"    
d = """
       </center></th>
       <th><img src="windspeed.png" alt="loading please wait...">
       <center style="color: red; font-family:calibri ;font-size:23px;">
       """
mess4=f"{messageWS}"   
e= """
       </center></th>
       <th><img src="airpressure.png" alt="loading please wait...">
       <center style="color: red; font-family:calibri ;font-size:23px;">
       """
mess5=f"{messageAirp}"    
f="""
       </center></th>  
       </tr>
       </tbody>
       </table>
       </center>
       <br></br><br></br>
       </body>
       """
print(a + mess1+b + mess2+c + mess3+d + mess4+e + mess5+ f)


















'''
<script>
function autoRefresh() {
       window.location = window.location.href;
       }
       setInterval('autoRefresh()', 1000);
</script>
'''
