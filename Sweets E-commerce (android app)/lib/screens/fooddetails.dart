import 'package:auto_size_text/auto_size_text.dart';
import 'package:firstapp/shared/Constants.dart';
import 'package:flutter/Material.dart';
import 'package:firstapp/shared/maindrawer.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:http/http.dart';
import 'dart:convert';
import 'dart:core';
import 'package:google_fonts/google_fonts.dart';

class FoodDeets extends StatefulWidget {
  final String foodurl;

  FoodDeets({Key key, @required this.foodurl}) : super(key: key);
  

  @override
  
  _FoodDeets createState() => _FoodDeets(foodurl);
}
class _FoodDeets extends State<FoodDeets> {
    Map foodarr;
    String foodurl;
    String alternate;
    String area;
    String ingredients;
    String foodname;
    String category;
    String foodIns;
    String foodpic;
    String source;
    String imgsource;
    String creativecommons;
    String datemodified;
    double length;
    String foodingred;
    String foodm;
    List<String> foodIngredients = [];
    _FoodDeets(this.foodurl);

  Future<Response> getFooddata() async {
    Response response = await get(Uri.parse(foodurl));
    return response;
  }
  @override
  void initState(){
    super.initState();
    getFooddata().then((value) {
      Map data = jsonDecode(value.body);      
      setState((){
        foodarr = data["meals"][0];
        area = foodarr['strArea'];
        foodname = foodarr['strMeal'];
        category = foodarr['strCategory'];
        foodIns = foodarr['strInstructions'];
        foodpic = foodarr['strMealThumb'];
        alternate = foodarr['strDrinkAlternate'];
        source = foodarr["strSource"];
        imgsource = foodarr["strImageSource"];
        creativecommons = foodarr["strCreativeCommonsConfirmed"];
        datemodified = foodarr["dateModified"]; 
        length = ((foodarr.length - 13)/2);
        for(int i=1; i<length; i++){
          if(foodarr['strMeasure$i'] != ""){
            foodIngredients.add(foodarr['strMeasure$i']);
            foodIngredients.add(" - ");
            foodIngredients.add(foodarr['strIngredient$i']);
            foodIngredients.add("\n");
          }          
        }
        foodIngredients.remove("   - ");
        ingredients = foodIngredients.join("");
          }
          ); 
          });
  }
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size; 
    return Scaffold(    
      backgroundColor: myColors,
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
        title: Text("Item Name",       
        style: TextStyle(
                   fontSize: 17,
                   fontWeight: FontWeight.bold,
                   color: myColors,
                  ), ),
 
      ), 
      body: 
      Stack(
        children: [
          SingleChildScrollView(
            scrollDirection: Axis.vertical,
            child: 
            Column(
              mainAxisSize: MainAxisSize.max, 
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 5),
                Container(
                margin: EdgeInsets.only(left: 5),
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
                          child: Text("<Back", 
                          style: TextStyle(
                                color: myColors,
                                fontSize: 14,
                                fontWeight: FontWeight.bold,             
                                ),),
                                onPressed: (){
                                Navigator.pushNamed(context, "/food");
                                },
                                ),) ,                             
                                ),
                                SizedBox(height: 7,),
                                foodpic != null ?
                                Container(
                                  height: screenSize.height *2.5,
                                  margin: EdgeInsets.only(left: 5, right: 5),
                                  //color: Colors.white,
                                  decoration: BoxDecoration(
                                  color: Colors.white,
                                  border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(30)),), 
                                  child: 
                                  Column(
                                    children: [
                                      Container(margin : EdgeInsets.all(10),
                                      child: 
                                           ClipRRect(
                                                    borderRadius: BorderRadius.circular(30),
                                                    child: Image(image: NetworkImage(foodpic),),
                                                )),
                                          Row(
                                              children: [Container(width: 120, 
                                                          child: 
                                                          Container(//foodname
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//pink
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Food Name ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                                            Container(//foodname
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    width: 240,    
                                                                      child: 
                                                                      Align(
                                                                      alignment: Alignment.centerLeft,
                                                                      child: 
                                                                      AutoSizeText(
                                                                        "   $foodname",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        //letterSpacing: 5,
                                                                        color: Colors.black,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.w900,
                                                                      ),
                                                                  ),),
                                                                  ),
                                                            ],),
                                          SizedBox(height:7),
                                          Row(//category
                                              children: [Container(width: 120, 
                                                          child: 
                                                          Container(//category
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Category ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                                            Container(//category
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    width: 240,    
                                                                      child: 
                                                                      Align(alignment: Alignment.centerLeft,child: 
                                                                      AutoSizeText(
                                                                        "   $category",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.black,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.w900,
                                                                      ),
                                                                  ),),
                                                                  ),
                                                            ],)
                                                            ,//foodcategory

                                          alternate != null?
                                          Row(//drink alternate
                                              children: [Container(width: 120, 
                                                          child: 
                                                          Container(//drink alternate
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Drinks ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                                            Container(//drink alternate
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    width: 240,    
                                                                      child: 
                                                                      Align(alignment: Alignment.centerLeft,child: 
                                                                      AutoSizeText(
                                                                        "   $alternate",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.black,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.w900,
                                                                      ),
                                                                  ),),
                                                                  ),
                                                            ],): Container(),//drink alternate
                                          SizedBox(height:7),
                                          Row(//Area
                                              children: [Container(width: 120, 
                                                          child: 
                                                          Container(//Area
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Area ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                                            Container(//Area
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    width: 240,
                                                                      child: 
                                                                      Align(alignment: Alignment.centerLeft,child: 
                                                                      AutoSizeText(
                                                                        "   $area",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.black,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.w900,
                                                                      ),
                                                                  ),),
                                                                  ),
                                                            ],),//area
                                          SizedBox(height:7),
                                          Column(                               //Ingredients start
                                          mainAxisSize: MainAxisSize.max, 
                                          mainAxisAlignment: MainAxisAlignment.start,
                                          crossAxisAlignment: CrossAxisAlignment.start,
                                          children: 
                                          [Container(width: 200, 
                                          child: 
                                          Container(//Ingredients
                                                      margin: EdgeInsets.only(left: 10),
                                                      height: 35,
                                                      decoration: BoxDecoration(
                                                      color: myColors,//Colors.pink[400],
                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                      ),      
                                                      child: 
                                                      Center(child: 
                                                      AutoSizeText(
                                                            "Ingredients ",
                                                             maxLines:2,
                                                             style:
                                                             GoogleFonts.manrope(
                                                             color: Colors.white,
                                                             textStyle: Theme.of(context).textTheme.headline4,
                                                             fontSize: 16,
                                                             fontWeight: FontWeight.bold,
                                                         ),
                                                      ),),
                                                  ),
                                          ),
                                          Container(//Ingredients
                                                      margin: EdgeInsets.only(left: 7, right: 3,top: 10),
                                                      height: 250,
                                                      child: 
                                                      SingleChildScrollView(
                                                        scrollDirection: Axis.vertical,
                                                        child: 
                                                        Align(
                                                        alignment: Alignment.centerLeft,
                                                        child: 
                                                        Container(
                                                          margin: EdgeInsets.only(left: 6, right: 12),
                                                          height: 300,
                                                          decoration: BoxDecoration(
                                                          color: Colors.white,
                                                          border: Border.all(
                                                                  color: myColors,//Colors.pink[400],
                                                                  width: 2,         
                                                                  ),
                                                                  borderRadius: 
                                                                  BorderRadius.all(
                                                                        Radius.circular(10)
                                                                        ),
                                                                  ),
                                                          child:
                                                          Container(
                                                            margin: EdgeInsets.only(left:7, right: 7,top:3),
                                                            child: Align(
                                                            alignment: Alignment.topLeft,
                                                            child:
                                                            AutoSizeText(
                                                              ingredients,
                                                              textAlign: TextAlign.justify,
                                                              style:
                                                              GoogleFonts.manrope(
                                                              color: Colors.black,
                                                              textStyle: Theme.of(context).textTheme.headline4,
                                                              fontSize: 14,
                                                              fontWeight: FontWeight.w900,
                                                              ),
                                                            ),),
                                                          ),
                                                      ),
                                                      ),
                                                      ),
                                                  ),
                                                  ]    
                                          ),          //Ingredients ends 
                                          SizedBox(height:30),
                                          Column(                               //Insturction start
                                          mainAxisSize: MainAxisSize.max, 
                                          mainAxisAlignment: MainAxisAlignment.start,
                                          crossAxisAlignment: CrossAxisAlignment.start,
                                          children: 
                                          [Container(width: 200, 
                                          child: 
                                          Container(//Insturction
                                                      margin: EdgeInsets.only(left: 10),
                                                      height: 35,
                                                      decoration: BoxDecoration(
                                                      color: myColors,//Colors.pink[400],
                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                      ),      
                                                      child: 
                                                      Center(child: 
                                                      AutoSizeText(
                                                            "Instructions ",
                                                             maxLines:2,
                                                             style:
                                                             GoogleFonts.manrope(
                                                             color: Colors.white,
                                                             textStyle: Theme.of(context).textTheme.headline4,
                                                             fontSize: 16,
                                                             fontWeight: FontWeight.bold,
                                                         ),
                                                      ),),
                                                  ),
                                          ),
                                          Container(//Insturction
                                                      margin: EdgeInsets.only(left: 7, right: 3,top: 10),
                                                      height: 400,
                                                      child: 
                                                      SingleChildScrollView(
                                                        scrollDirection: Axis.vertical,
                                                        child: 
                                                        Align(
                                                        alignment: Alignment.centerLeft,
                                                        child: 
                                                        Container(
                                                          margin: EdgeInsets.only(left: 6, right: 12),
                                                          height: 900,
                                                          decoration: BoxDecoration(
                                                          color: Colors.white,
                                                          border: Border.all(
                                                                  color: myColors,//Colors.pink[400],
                                                                  width: 2,         
                                                                  ),
                                                                  borderRadius: 
                                                                  BorderRadius.all(
                                                                        Radius.circular(10)
                                                                        ),
                                                                  ),
                                                          child:
                                                          Container(
                                                            margin: EdgeInsets.only(left:7, right: 7,top:3),
                                                            child: Align(
                                                            alignment: Alignment.topLeft,
                                                            child:
                                                            AutoSizeText(
                                                              foodIns,
                                                              textAlign: TextAlign.justify,
                                                              style:
                                                              GoogleFonts.manrope(
                                                              color: Colors.black,
                                                              textStyle: Theme.of(context).textTheme.headline4,
                                                              fontSize: 14,
                                                              fontWeight: FontWeight.w900,
                                                              ),
                                                            ),),
                                                          ),
                                                      ),
                                                      ),
                                                      ),
                                                  ),
                                                  ]    
                                          ),                                                //Instruction end
                                          SizedBox(height:30),
                                          source != null?
                                          Column(children: [
                                          Container(margin: EdgeInsets.only(right:260,top:5),  child: 
                                                 Container(
                                                          child: 
                                                          Container(//sourcelink
                                                                    margin: EdgeInsets.only(left: 12),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Source  ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                          ),//sourcelink
                                          Container(//sourcelink
                                                      margin: EdgeInsets.only(top:10,left: 10, right: 10),
                                                      child: 
                                                      Align(
                                                      alignment: Alignment.centerLeft,
                                                      child: 
                                                      Container(
                                                        margin: EdgeInsets.only(left: 6, right: 12),
                                                        child:
                                                        AutoSizeText(
                                                             source,
                                                             maxLines: 2,
                                                             style:
                                                             GoogleFonts.manrope(
                                                             color: Colors.black,
                                                             textStyle: Theme.of(context).textTheme.headline4,
                                                             fontSize: 14,
                                                             fontWeight: FontWeight.w900,
                                                         ),
                                                      ),
                                                      ),
                                                      ),
                                                  ),
                                          
                                          ],) :Container(),
                                          SizedBox(height:7),
                                          imgsource != null?
                                          Column(children: [
                                          Container(margin: EdgeInsets.only(right:250,top:20), width: 120, child: 
                                          Container(width: 120, 
                                                          child: 
                                                          Container(//sourcelink
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Img Source ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                          ),//sourcelinkIMAGE
                                          Container(//sourcelinkIMAGE
                                                      margin: EdgeInsets.only(top:10,left: 10, right: 10),
                                                      child: 
                                                      Align(
                                                      alignment: Alignment.centerLeft,
                                                      child: 
                                                      Container(
                                                        margin: EdgeInsets.only(left: 6, right: 12),
                                                        child:
                                                        AutoSizeText(
                                                             imgsource,
                                                             maxLines: 2,
                                                             style:
                                                             GoogleFonts.manrope(
                                                             color: Colors.black,
                                                             textStyle: Theme.of(context).textTheme.headline4,
                                                             fontSize: 14,
                                                             fontWeight: FontWeight.w900,
                                                         ),
                                                      ),
                                                      ),
                                                      ),
                                                  ),
                                          
                                          ],) :Container(), 
                                          SizedBox(height:7),
                                          creativecommons!= null?
                                          Column(children: [
                                          Container(margin: EdgeInsets.only(right:115,top:20), width: 120, child: 
                                          Container(width: 200, 
                                                          child: 
                                                          Container(//creativecommons
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Creative commons confirmed ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                          ),//creativecommons
                                          Container(//creativecommons
                                                      margin: EdgeInsets.only(top:10,left: 10, right: 10),
                                                      child: 
                                                      Align(
                                                      alignment: Alignment.centerLeft,
                                                      child: 
                                                      Container(
                                                        margin: EdgeInsets.only(left: 6, right: 12),
                                                        child:
                                                        AutoSizeText(
                                                             creativecommons,
                                                             maxLines: 2,
                                                             style:
                                                             GoogleFonts.manrope(
                                                             color: Colors.black,
                                                             textStyle: Theme.of(context).textTheme.headline4,
                                                             fontSize: 14,
                                                             fontWeight: FontWeight.w900,
                                                         ),
                                                      ),
                                                      ),
                                                      ),
                                                  ),
                                          ],) :Container(),
                                          SizedBox(height:3),
                                          datemodified != null?
                                          Column(children: [
                                          Container(margin: EdgeInsets.only(right:180,top:20), width: 120, child: 
                                          Container(width: 200, 
                                                          child: 
                                                          Container(//datemodified
                                                                    margin: EdgeInsets.only(left: 10),
                                                                    height: 35,
                                                                    decoration: BoxDecoration(
                                                                      color: myColors,//Colors.pink[400],
                                                                      border: Border.all(color: Colors.white),borderRadius: BorderRadius.all(Radius.circular(7))                                                                     
                                                                      ),      
                                                                      child: 
                                                                      Center(child: 
                                                                      AutoSizeText(
                                                                        "Date Modified ",
                                                                        maxLines:2,
                                                                        style:
                                                                        GoogleFonts.manrope(
                                                                        color: Colors.white,
                                                                        textStyle: Theme.of(context).textTheme.headline4,
                                                                        fontSize: 16,
                                                                        fontWeight: FontWeight.bold,
                                                                      ),
                                                                  ),),
                                                                  ),),
                                          ),//datemodified
                                          Container(//datemodified
                                                      margin: EdgeInsets.only(top:10,left: 10, right: 10),
                                                      child: 
                                                      Align(
                                                      alignment: Alignment.centerLeft,
                                                      child: 
                                                      Container(
                                                        margin: EdgeInsets.only(left: 6, right: 12),
                                                        child:
                                                        AutoSizeText(
                                                             datemodified,
                                                             maxLines: 2,
                                                             style:
                                                             GoogleFonts.manrope(
                                                             color: Colors.black,
                                                             textStyle: Theme.of(context).textTheme.headline4,
                                                             fontSize: 14,
                                                             fontWeight: FontWeight.w900,
                                                         ),
                                                      ),
                                                      ),
                                                      ),
                                                  ),
                                          ],) :Container(),                              
                                    ],
                                  )             
                                  )
                                  :Center(child: SpinKitDoubleBounce(color: Colors.white,),),                          
                  ],
                ),
              ),
      ],),
    );
  }
}