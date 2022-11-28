import 'package:firstapp/shared/Constants.dart';
import 'package:flutter/material.dart';
void main() => runApp(
  MaterialApp( 
    debugShowCheckedModeBanner: false,
    theme: ThemeData(splashColor: Colors.white, primaryColor: Colors.white),
      
  )
);

class MainDrawer extends StatelessWidget {
   
  @override
 

  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;    
    return new Drawer(
      child: Column(
        children: [         
          Container(
            width: double.infinity,
            height: screenSize.height,
            padding: EdgeInsets.all(20),
            color: myColors,
            child: Center(
              child: Column(
                children: [
                  Container(
                    width: 130,
                    height: 100,
                    margin: EdgeInsets.only(top: 50),
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(
                        image: AssetImage("assets/rhee.jpg"),
                        fit: BoxFit.fill
                      )
                    ),
                  ),
                  SizedBox(height: 20,),
                  Text("Rhee Jan A. Talo", style: TextStyle(letterSpacing: .4 ,fontWeight: FontWeight.bold, fontSize: 17),),
                  Text("January 03, 2001", style: TextStyle(letterSpacing: .4 ,fontStyle: FontStyle.italic , fontSize: 16),),
                  SizedBox(height: 20,),
                  Text("BS-IS", style: TextStyle(letterSpacing: .4 ,fontSize: 16),),
                  Text("Atene de Davao", style: TextStyle(letterSpacing: .4 ,fontSize: 16),),
                  Text("University", style: TextStyle(letterSpacing: .4 ,fontSize: 16),),
                  SizedBox(height: 330, ),
                  Align(
                    alignment: Alignment.bottomRight,
                    child: Container(
                            decoration: BoxDecoration(
                                color: myColors,
                                boxShadow: [
                                BoxShadow(
                                  color: Colors.grey[700],
                                  offset: Offset(0,2),
                                  blurRadius: 2,
                                  spreadRadius: 2
                                        )
                                      ]
                                  ),               
                            child:
                            SizedBox(
                              width : screenSize.width * .21,
                              height: screenSize.height * .04,
                            child: 
                            RaisedButton(
                                color: Colors.white,
                                child: Text("Log out", 
                                style: TextStyle(
                                        color: myColors,
                                        fontSize: 14,
                                        fontWeight: FontWeight.bold,             
                                ),),
                                onPressed: (){
                                  Navigator.pushNamedAndRemoveUntil(context, '/',ModalRoute.withName('/'));  
                                  },
                                ),)                                   
                            ),
                  )
                ],
              ),
              
            ),
          ),
        ],
      ),

    );
  }
}
