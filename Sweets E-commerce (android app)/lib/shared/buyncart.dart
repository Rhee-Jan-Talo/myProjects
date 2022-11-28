import 'package:firstapp/shared/Constants.dart';
import 'package:flutter/material.dart';

void main() => runApp(
  MaterialApp( 
    debugShowCheckedModeBanner: false,
    theme: ThemeData(splashColor: Colors.white, primaryColor: Colors.white),
      
  )
);

class BuynCart extends StatelessWidget {
   
  @override

  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;    
    return FlatButton
            (
            child:
            Row(
              children: 
              [
                Row(
                  children: [
                    Container(
                      margin: EdgeInsets.only(left: 8),
                      decoration: BoxDecoration(
                      border:Border.all(color: myColors, width: 2),
                      color: Colors.white,
                      
                      ),               
                      child:
                          SizedBox(
                          width : 60,
                          height: 35,
                          child: 
                              RaisedButton(
                                color: Colors.white,
                                child: Text("Buy", 
                                style: TextStyle(
                                      color: Colors.black,
                                      fontSize: 13,
                                      fontWeight: FontWeight.bold,             
                                      ),),
                                      onPressed: (){
                                      
                                      },
                                      ),)                                   
                                      ),
                        Container(
                          margin: EdgeInsets.only(left: 5),
                          decoration: BoxDecoration(
                          color: myColors,
                         // border: Border.all(color: myColors,width: 2),
                          ),               
                          child:
                              SizedBox(
                              width : 60,
                              height: 35,
                              child: 
                                  RaisedButton(
                                    color: myColors,
                                    child: Text("Cart", 
                                    style: TextStyle(
                                          color: Colors.white,
                                          fontSize: 13,
                                          fontWeight: FontWeight.bold,             
                                          ),),
                                          onPressed: (){
                                          
                                          },
                                          ),)                                   
                                          ),
                ],),
              ],
            ),
      onPressed: () {},   
    );
  }
}
