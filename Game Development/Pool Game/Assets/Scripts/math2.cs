using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class math2 : MonoBehaviour
{
    public TextMeshPro t1;
    public TextMeshPro t2;
    public TextMeshPro t3;
    public TextMeshPro t4;
    public TextMeshPro t5;
    public TextMeshPro ans1;
    public TextMeshPro ans2;
    public TextMeshPro ans3;
    public TextMeshPro ans4;
    public TextMeshPro ans5;
    public TextMeshPro ans6;
    public TextMeshPro ans7;
    public TextMeshPro ans8;
    public TextMeshPro final1;
    public TextMeshPro final2;
    public TextMeshPro final3;
    public TextMeshPro final4;
    public TextMeshPro final5;
    public TextMeshPro final6;

    public GameObject SoftStar;
    public GameObject Diamondo5side;
    public GameObject SphereGemLarge;
    public GameObject Heart;
    public GameObject Hexgon;
    public GameObject Spiral;
    public GameObject Cuboid;
    public GameObject Penta;
    public GameObject CubieBeveled;
    public GameObject Hardstar;

              
    int [] numbers = new int[5] {0,0,0,0,0};
    int j = 0;
    bool available = true;

    int a=0;
    int b=0;

    string z;//temp variables for finalans
    string x;//temp variables for finalans
    string y;//temp variables for finalans
    string n;//upper value sa ans
    string m;//lower value sa ans
    int aa,bb;//temp variables for ans
    int ans;//temp variable for final ans

    char[] fanslst;
    char[] anslst;

    string tryy;
    int _c = 0;

    void Start(){
        ans1.enabled = false;
        ans2.enabled = false;
        ans3.enabled = false;
        ans4.enabled = false;
        ans5.enabled = false;
        ans6.enabled = false;
        ans7.enabled = false;
        ans8.enabled = false;
        final1.enabled = false;
        final2.enabled = false;
        final3.enabled = false;
        final4.enabled = false;
        final5.enabled = false;
        final6.enabled = false;

    }
    void Update()
    {   
        
        if(j<5){
            randomizer2();
        }
        
        
        t1.SetText(numbers[0].ToString());
        t2.SetText(numbers[1].ToString());
        t3.SetText(numbers[2].ToString());
        t4.SetText(numbers[3].ToString());
        t5.SetText(numbers[4].ToString());
        solveans1();
        solveans2();
        solvefans();
        //print(t1.text);
        if(j==5){
            if(_c==0)
            {
                showshapes();
            }
            _c=1;
        }
        
    }
    public void randomizer2(){
        available = false;
        int randint = Random.Range(1,9);
        for(int i=0; i<5; i++)
            {
            if(randint==numbers[i])
                {
                    available = true;
                }
            }
        if(available == false)
            {
                numbers[j] = randint;
                j++;
            }
    }

    public void solveans1(){
        aa = int.Parse(string.Concat(numbers[2].ToString(),numbers[1].ToString(),numbers[0].ToString()));
        n = (aa * numbers[3]).ToString();
        //print(n);
        displayans1();
    }

    public void solveans2(){
        bb = int.Parse(string.Concat(numbers[2].ToString(),numbers[1].ToString(),numbers[0].ToString()));
        m = (bb * numbers[4]).ToString();
        //print(m);
        displayans2();
    }

    public void solvefans(){
        getvalues();
        ans = a * b; 
        displayFans();
    }

    public void displayFans(){
        fanslst = ans.ToString().ToCharArray();
        if(fanslst.Length == 4){
            final1.SetText(fanslst[3].ToString());
            final2.SetText(fanslst[2].ToString());
            final3.SetText(fanslst[1].ToString());
            final4.SetText(fanslst[0].ToString());
            final5.SetText(" ");
            final6.SetText(" ");
        }
        if(fanslst.Length == 5){
            final1.SetText(fanslst[4].ToString());
            final2.SetText(fanslst[3].ToString());
            final3.SetText(fanslst[2].ToString());
            final4.SetText(fanslst[1].ToString());
            final5.SetText(fanslst[0].ToString());
            final6.SetText(" ");
        }
        if(fanslst.Length == 6){
            final1.SetText(fanslst[5].ToString());
            final2.SetText(fanslst[4].ToString());
            final3.SetText(fanslst[3].ToString());
            final4.SetText(fanslst[2].ToString());
            final5.SetText(fanslst[1].ToString());
            final6.SetText(fanslst[0].ToString());
        }
    }

    public void displayans1(){
        if(n.Length == 4){
            ans1.SetText(n[3].ToString());
            ans2.SetText(n[2].ToString());
            ans3.SetText(n[1].ToString());
            ans4.SetText(n[0].ToString());
        }
        if(n.Length == 3){
            ans1.SetText(n[2].ToString());
            ans2.SetText(n[1].ToString());
            ans3.SetText(n[0].ToString());
            ans4.SetText(" ");
        }
    }

    public void displayans2(){
        if(m.Length == 4){
            ans5.SetText(m[3].ToString());
            ans6.SetText(m[2].ToString());
            ans7.SetText(m[1].ToString());
            ans8.SetText(m[0].ToString());
        }
        if(m.Length == 3){
            ans5.SetText(m[2].ToString());
            ans6.SetText(m[1].ToString());
            ans7.SetText(m[0].ToString());
            ans8.SetText(" ");
        }
    }

    public void getvalues(){
        x = numbers[4].ToString();
        y = numbers[3].ToString();
        b = int.Parse(string.Concat(x,y));
        x = numbers[0].ToString();
        y = numbers[1].ToString();
        z = numbers[2].ToString();
        a = int.Parse(string.Concat(z,y,x));
    }

    public void showshapes(){
        
        


        Instantiate(shape(int.Parse(ans1.text)),new Vector3(17.72f,14.39f,23.61f), shape(int.Parse(ans1.text)).transform.rotation);//ans1
        Instantiate(shape(int.Parse(ans2.text)),new Vector3(16.93f, 14.39f, 23.61f), shape(int.Parse(ans2.text)).transform.rotation);//ans2
        Instantiate(shape(int.Parse(ans3.text)),new Vector3(16.11f, 14.39f, 23.61f), shape(int.Parse(ans3.text)).transform.rotation);//ans3
        if(ans4.text != " ")Instantiate(shape(int.Parse(ans4.text)),new Vector3(15.3f,  14.39f, 23.61f), shape(int.Parse(ans4.text)).transform.rotation);//ans4
        
        Instantiate(shape(int.Parse(ans5.text)),new Vector3(16.91f, 13.45f, 23.61f), shape(int.Parse(ans5.text)).transform.rotation);//ans5
        Instantiate(shape(int.Parse(ans6.text)),new Vector3(16.11f, 13.45f, 23.61f), shape(int.Parse(ans6.text)).transform.rotation);//ans6
        Instantiate(shape(int.Parse(ans7.text)),new Vector3(15.28f, 13.45f, 23.61f), shape(int.Parse(ans7.text)).transform.rotation);//ans7
        if(ans8.text != " ")Instantiate(shape(int.Parse(ans8.text)),new Vector3(14.45f, 13.45f, 23.61f), shape(int.Parse(ans8.text)).transform.rotation);

        Instantiate(shape(int.Parse(final1.text)),new Vector3(17.8f, 11.73f, 23.61f), shape(int.Parse(final1.text)).transform.rotation);//fans1
        Instantiate(shape(int.Parse(final2.text)),new Vector3(16.94f, 11.73f, 23.61f), shape(int.Parse(final2.text)).transform.rotation);//fans2
        Instantiate(shape(int.Parse(final3.text)),new Vector3(16.11f, 11.73f, 23.61f), shape(int.Parse(final3.text)).transform.rotation);//fans3
        Instantiate(shape(int.Parse(final4.text)),new Vector3(15.3f, 11.73f, 23.61f), shape(int.Parse(final4.text)).transform.rotation);//fans4
        if(final5.text != " ")Instantiate(shape(int.Parse(final5.text)),new Vector3(14.45f, 11.73f, 23.61f), shape(int.Parse(final5.text)).transform.rotation);
        if(final6.text != " ")Instantiate(shape(int.Parse(final6.text)),new Vector3(13.64f, 11.73f, 23.61f), shape(int.Parse(final6.text)).transform.rotation);

        
    }
    public GameObject shape(int a){

            if(a==1)//SoftStar
                return SoftStar;
            else if(a==2)//Diamondo5side
                return Diamondo5side;
                
            else if(a==3)//Spiral
                return Spiral;
                
            else if(a==4)//SphereGemLarge
                return SphereGemLarge;
                
            else if(a==5)//Heart
                return Heart;
                
            else if(a==6)//Hexgon
                return Hexgon;
                
            else if(a==7)//Cuboid
                return Cuboid;
                
            else if(a==8)//Penta
                return Penta;
                
            else if(a==9)//CubieBeveled
                return CubieBeveled;
                
            else{
                return Hardstar;
                }
                

        }
}

/*
    

        GameObject _1 = shape(int.Parse(ans1.text));
        GameObject _2 = shape(int.Parse(ans2.text));
        GameObject _3 = shape(int.Parse(ans3.text));
        GameObject _4 = shape(int.Parse(ans4.text));
        GameObject _5 = shape(int.Parse(ans5.text));
        GameObject _6 = shape(int.Parse(ans6.text));
        GameObject _7 = shape(int.Parse(ans7.text));
        GameObject _8 = shape(int.Parse(ans8.text));

        GameObject _9 = shape(int.Parse(final1.text));
        GameObject _10 = shape(int.Parse(final2.text));
        GameObject _11 = shape(int.Parse(final3.text));
        GameObject _12 = shape(int.Parse(final4.text));
        GameObject _13 = shape(int.Parse(final5.text));
        GameObject _14 = shape(int.Parse(final6.text));


        17.54f,14.39f,23.61f
        16.93f, 14.39f, 23.61f
        16.11f, 14.39f, 23.61f
        15.3f,  14.39f, 23.61f

        16.91f, 13.45f, 23.61f
        16.11f,f, 13.45f, 23.61f
        15.28f, 13.45f, 23.61f
        14.45f, 13.45f, 23.61f

        17.8f, 11.73f, 23.61f
        16.94f, 11.73f, 23.61f
        16.11f, 11.73f, 23.61f
        15.3f, 11.73f, 23.61f
        14.45f, 11.73f, 23.61f
        13.64f, 11.73f, 23.61f

        Instantiate(Heart,new Vector3(17.72f,14.39f,23.61f), Heart.transform.rotation);//ans1
        Instantiate(Heart,new Vector3(16.93f, 14.39f, 23.61f), Heart.transform.rotation);//ans2
        Instantiate(Heart,new Vector3(16.11f, 14.39f, 23.61f), Heart.transform.rotation);//ans3
        Instantiate(Heart,new Vector3(15.3f,  14.39f, 23.61f), Heart.transform.rotation);//ans4

        Instantiate(Heart,new Vector3(16.91f, 13.45f, 23.61f), Heart.transform.rotation);//ans5
        Instantiate(Heart,new Vector3(16.11f, 13.45f, 23.61f), Heart.transform.rotation);//ans6
        Instantiate(Heart,new Vector3(15.28f, 13.45f, 23.61f), Heart.transform.rotation);//ans7
        Instantiate(Heart,new Vector3(14.45f, 13.45f, 23.61f), Heart.transform.rotation);//ans8

        Instantiate(Heart,new Vector3(17.8f, 11.73f, 23.61f), Heart.transform.rotation);//fans1
        Instantiate(Heart,new Vector3(16.94f, 11.73f, 23.61f), Heart.transform.rotation);//fans2
        Instantiate(Heart,new Vector3(16.11f, 11.73f, 23.61f), Heart.transform.rotation);//fans3
        Instantiate(Heart,new Vector3(15.3f, 11.73f, 23.61f), Heart.transform.rotation);//fans4
        Instantiate(Heart,new Vector3(14.45f, 11.73f, 23.61f), Heart.transform.rotation);//fans5
        Instantiate(Heart,new Vector3(13.64f, 11.73f, 23.61f), Heart.transform.rotation);//fans6
        

        

        Instantiate(SoftStar,new Vector3(17.72f,14.39f,23.61f), SoftStar.transform.rotation);//ans1
        Instantiate(Spiral,new Vector3(16.93f, 14.39f, 23.61f), Diamondo5side.transform.rotation);//ans2
        Instantiate(SphereGemLarge,new Vector3(16.11f, 14.39f, 23.61f), SphereGemLarge.transform.rotation);//ans3
        Instantiate(Heart,new Vector3(15.3f,  14.39f, 23.61f), Heart.transform.rotation);//ans4

        Instantiate(Diamondo5side,new Vector3(16.91f, 13.45f, 23.61f), Diamondo5side.transform.rotation);//ans5
        Instantiate(Hexgon,new Vector3(16.11f, 13.45f, 23.61f), Hexgon.transform.rotation);//ans6
        Instantiate(Heart,new Vector3(15.28f, 13.45f, 23.61f), Heart.transform.rotation);//ans7
        Instantiate(Cuboid,new Vector3(14.45f, 13.45f, 23.61f), Cuboid.transform.rotation);//ans8

        Instantiate(Penta,new Vector3(17.8f, 11.73f, 23.61f), Penta.transform.rotation);//fans1
        Instantiate(Heart,new Vector3(16.94f, 11.73f, 23.61f), Heart.transform.rotation);//fans2
        Instantiate(Heart,new Vector3(16.11f, 11.73f, 23.61f), Heart.transform.rotation);//fans3
        Instantiate(Heart,new Vector3(15.3f, 11.73f, 23.61f), Heart.transform.rotation);//fans4
        Instantiate(Heart,new Vector3(14.45f, 11.73f, 23.61f), Heart.transform.rotation);//fans5
        Instantiate(CubieBeveled,new Vector3(13.64f, 11.73f, 23.61f), CubieBeveled.transform.rotation);//fans6

        */