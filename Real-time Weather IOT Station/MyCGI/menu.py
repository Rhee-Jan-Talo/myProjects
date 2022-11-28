

print("Content-Type: text/html\n")
a="""
<head>
<style>
p {margin: 25px 50px 25px 445px;}
h1{margin: 150px;}
</style>
</head>
<body>


<center>
<form method="POST" action="sample.py">
<h1></h1>
<h2>Welcome To Weather Station IOT</h2>
<p><button type ="submit"
       style="height:35px; width:150px; color: black; font-size:16px; border-radius: 10px; align: left; ">
       Go to Graphs</button></p>
</form>

       
<form method="POST" action="ave.py">
<label>Date From: </label><input type="date" format="dd/mm/yyyy" name="date1" required>
<label>to: </label><input type="date" name="date2" required>
<button type ="submit"
       style="height:35px; width:150px; color: black; font-size:16px; border-radius: 10px; ">
       Calculte Average</button>
</form>

</center>





</body>

     """
print(a)
