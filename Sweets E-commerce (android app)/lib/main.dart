import 'package:firstapp/FA/mainmenu.dart';
import 'package:firstapp/FA/screen2.dart';
import 'package:firstapp/screens/foodscreen.dart';
import 'package:firstapp/shared/Constants.dart';
import 'package:firstapp/screens/fooddetails.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


void main() => runApp(
  MaterialApp( 
    debugShowCheckedModeBanner: false,
    theme: ThemeData(splashColor: Colors.white, primaryColor: Colors.white),
    routes: {
      '/' : (context) => HomeScreen(),
      '/second' : (context) => SecondScreen(),
      '/menu' : (context) => Mainmenu(),
      '/food' : (context) => Foodscreen(),
      '/deets': (context) => FoodDeets(foodurl: ""),
    }
      
  )
);

class HomeScreen extends StatelessWidget {
   
  @override
 

  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;
    return Scaffold(
    resizeToAvoidBottomInset : false,     
    backgroundColor: myColors,
      body: 
      Column(
        mainAxisSize: MainAxisSize.max, 
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Column(children: [               
              Container(
                
                padding: EdgeInsets.symmetric(vertical: 70, horizontal: 50),              
                color: myColors,
                
              ),
            Container( 
              width: screenSize.width,
              color: myColors,
              child: 
                Column(children: [
                Text("LOGIN",                   
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 35,
                    fontWeight: FontWeight.bold,
                    letterSpacing: .7,
                  )                 
                  )
              ],),),
            Container( 
              width: screenSize.width,
              color: myColors,
              child: 
                Column(children: [
                Text("TO CONTINUE", 
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.w700,
                    fontSize: 16.5,
                    letterSpacing: 8,
                  )                  
                  )
              ],),
              )    
          ],
          ),
          Container( 
              padding: EdgeInsets.symmetric(vertical: 70, horizontal: 50),
              width: screenSize.width,
              color: myColors,              
              child: 
                Column(
                  mainAxisSize: MainAxisSize.max, 
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,                 
                  children:
                   [                    
                    TextField(
                      decoration: InputDecoration(
                        hintText: "username",
                        hintStyle: TextStyle(
                          color: Colors.white,
                          fontSize: 13,
                        ),
                        enabledBorder: UnderlineInputBorder(      
                          borderSide: BorderSide(color: Colors.white, width: 2),   
                          ),  
                        focusedBorder: UnderlineInputBorder(
                        borderSide: BorderSide(color: Colors.white, width: 2),
                        ),
                        ),
                        keyboardType:  TextInputType.visiblePassword,
                        ),
    
                    TextField(
                      decoration: InputDecoration(
                        hintText: "your password",
                        hintStyle: TextStyle(
                          color: Colors.white,
                          fontSize: 13,
                        ),
                        enabledBorder: UnderlineInputBorder(      
                          borderSide: BorderSide(color: Colors.white, width: 4),   
                          ),  
                        focusedBorder: UnderlineInputBorder(
                        borderSide: BorderSide(color: Colors.white, width: 4),
                        ),
                        ),
                        keyboardType:  TextInputType.visiblePassword,
                        obscureText:true,                   
                      ),
                                Container(
                                  padding: EdgeInsets.symmetric(vertical: 55),
                                  color: myColors,
                                ),
                      Row(
                        mainAxisSize: MainAxisSize.max, 
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children:[
                          Container(      
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
                                  width : screenSize.width * .5,
                                  height: screenSize.height * .05,
                                  child: RaisedButton(
                                    color: Colors.white,
                                    shape: RoundedRectangleBorder(
                                              side: BorderSide(color: Colors.white),
                                              ),
                                    onPressed: (){
                                      Navigator.pushNamedAndRemoveUntil(context, '/food', ModalRoute.withName('/food  '));
                                    },
                                    splashColor: Colors.pinkAccent,
                                  child: Text("LOG IN", style: TextStyle(color: myColors, letterSpacing: 4,)
                                  ),                                  
                                ),                                
                                ),                                            
                              ),                             
                          ]
                      ), 
            
              
                                                         
              ],
              ),
              )
        ],
      )
    ); 
  }
}
