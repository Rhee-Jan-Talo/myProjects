import 'package:firstapp/shared/Constants.dart';
import 'package:flutter/Material.dart';

class ButtonWidget extends StatelessWidget {
  Size screenSize;
  
  /* 10-4 video
  final String title;
  const ButtonWidget({Key key, this.title}) : super(key: key);
  */

  @override
  Widget build(BuildContext context) {
    return Row
    
    (
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
                                  width : 80,
                                  height: 30,
                                  
                                  child: RaisedButton(
                                    color: Colors.white,
                                    shape: RoundedRectangleBorder(
                                              side: BorderSide(color: Colors.white),
                                              ),
                                    onPressed: (){
                                      
                                    },
                                    splashColor: Colors.pinkAccent,
                                  child: Text("Next >>", style: TextStyle(color: myColors, letterSpacing: 2, fontSize:14, fontWeight: FontWeight.bold, )
                                  ),                                  
                                ),                                
                                ),                                            
                              ),                             
                          ]
    );
                      
  }
}