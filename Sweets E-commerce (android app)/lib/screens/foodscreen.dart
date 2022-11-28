import 'package:firstapp/shared/Constants.dart';
import 'package:firstapp/shared/buyncart.dart';
import 'package:flutter/Material.dart';
import 'package:firstapp/screens/fooddetails.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'dart:core';
import 'package:firstapp/shared/maindrawer.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:auto_size_text/auto_size_text.dart';


class Foodscreen extends StatefulWidget {
  @override
  _Foodscreen createState() => _Foodscreen();
}

class _Foodscreen extends State<Foodscreen> {
  String foodUrl = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=Dessert';
  String url;
  dynamic foodurl;
  Map foodarr = new Map();
  String loader;
  String foodIDget;
  String foodID;
  List<dynamic> a = [];
  List <dynamic> foodP = [];
  List <dynamic> foodN = [];
  List <dynamic> foodI = [];

  Future<Response> getFooddata() async {
    Response response = await get(Uri.parse(foodUrl));
    return response;
  }
  void _onTileClicked(int index){
    index = index + 1;
    print("you clicked: $index");
  }
  @override
  
  void initState(){
    super.initState();
    
    getFooddata().then((value) {
      Map data = jsonDecode(value.body); 
      a = data["meals"];     
      setState((){
        url = 'https://www.themealdb.com/api/json/v1/1/lookup.php?i=';
        loader = "nyes";
        
        for (int i=0;i<a.length;i++){
          foodarr = data["meals"][i];
          foodN.add(foodarr['strMeal']);
          foodI.add(foodarr['idMeal']) ;
          foodP.add(foodarr['strMealThumb']);
        }          
      }
      ); 
      });
  }

  @override
  
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;
    return Scaffold(     
      backgroundColor: myColors,
      resizeToAvoidBottomInset : false,    
        endDrawer: new MainDrawer(),
        appBar: AppBar(
            automaticallyImplyLeading: false,
            actions: [
                Builder(
                  builder: (context) => IconButton(
                        icon: Icon(Icons.person),
                        onPressed: () => Scaffold.of(context).openEndDrawer(),
                        tooltip: MaterialLocalizations.of(context).openAppDrawerTooltip,
                      ),
                ),
              ],
            title: Text("Home",       
            style: TextStyle(
                         fontSize: 17,
                         fontWeight: FontWeight.bold,
                         color: myColors,
                      ),),
          ),   
          body: 
          Stack(
            children: [
              Container(
                width: screenSize.width,
                height: screenSize.height * .9,
                child:
                GridView.count(
                  crossAxisCount: 2,
                  childAspectRatio: (screenSize.width / 620),
                  crossAxisSpacing: 10,
                  padding: const EdgeInsets.all(10),
                  children: 
                    List.generate(a.length,(index){
                      return
                     Stack(
                        children: [
                          Container(
                          margin: EdgeInsets.only(top: 10),
                          width: screenSize.width * .5,
                          height: screenSize.height * .45,
                          child: 
                          loader != null
                          ?
                          InkWell(
                            child:
                            Container(  
                            decoration: BoxDecoration(
                              color: Colors.white,
                              border: Border.all(
                                      color: Colors.white,
                                      width: 2,         
                                      ),
                                      borderRadius: 
                                      BorderRadius.all(
                                            Radius.circular(10)
                                            ),
                                      ),
                                    child: 
                                    ClipRRect(
                                      borderRadius: BorderRadius.circular(10),
                                      child:
                                      Column(
                                        children: 
                                        [
                                        Container(//foodname
                                        margin: EdgeInsets.only(top:4, left:4, right:4),
                                        height: 45,
                                        decoration: BoxDecoration(
                                                    color: Colors.white,
                                                    border: Border.all(color: myColors, width: 2),borderRadius: BorderRadius.all(Radius.circular(5))                                                                     
                                                    ),      
                                                    child: 
                                                    Container(child: 
                                                    Center(child: 
                                                    AutoSizeText(
                                                          foodN[index],
                                                          maxLines:1,
                                                          style:
                                                          GoogleFonts.manrope(
                                                          //letterSpacing: 5,
                                                          color: Colors.black,
                                                          textStyle: Theme.of(context).textTheme.headline4,
                                                          fontSize: 14,
                                                          fontWeight: FontWeight.w900,
                                                          ),
                                                    ),),),
                                               ),
                                                Container(//foodpic
                                                margin: EdgeInsets.only(top:8),
                                                child: 
                                                ClipRRect(
                                                     borderRadius: BorderRadius.circular(10),
                                                     child: Image.network(foodP[index],
                                                     height: 140, width: 165,fit: BoxFit.fill),                                                    
                                                   )),                                            
                                                SizedBox(height: 4,),
                                                Container(child: Text("Php 150.00",//prices , 
                                                       style: 
                                                       GoogleFonts.manrope(
                                                       color: Colors.black,
                                                       textStyle: Theme.of(context).textTheme.headline4,
                                                       fontSize: 15,
                                                       fontWeight: FontWeight.w900,
                                                    ),)), 
                                                    SizedBox(height: 2,),
                                                   BuynCart(),
                                        ],
                                      ),
                                    ),
                                  ),
                          onTap:(){
                            foodIDget = foodI[index];
                            foodID = url+ foodIDget;
                            _onTileClicked(index);
                            foodurl = foodID;
                            Navigator.of(context).push(MaterialPageRoute (builder: (context) => FoodDeets(foodurl: foodurl)));
                          }
                          )
                           :Center(child: SpinKitDoubleBounce(color: Colors.white,),),  
                        ),
                        ],
                      );
                    }
                    )
                ), 
              ),
            ],
          ), 
    ); 
  }
}



/*

 */