using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ball : MonoBehaviour
{
    
    public GameObject wball_pre;
    public GameObject wball_pre2;
    
    public Rigidbody wball ;

   
    public float posx;
    public float posy;
    public float posz;

    
    
    void Start()
    {
       wball = gameObject.GetComponent<Rigidbody>();
    }

    
    void Update()
    {   

        if(wball.velocity==Vector3.zero && GameObject.FindGameObjectsWithTag("stick").Length <= 0){
            print("White ball stopped moving");
            posx = wball.transform.position.x;
            posy = wball.transform.position.y;
            posz = wball.transform.position.z;
            
            Instantiate(wball_pre, new Vector3(posx,posy,posz), wball_pre.transform.rotation);
            Destroy(gameObject);
        }
    }
}
/*
if(wball.velocity==Vector3.zero && GameObject.FindGameObjectsWithTag("stick").Length <= 0){
            print("White ball stopped moving");
            posx = wball.transform.position.x;
            posy = wball.transform.position.y;
            posz = wball.transform.position.z;
            //gameObject.SetActive(false);
            Destroy(gameObject);
            Instantiate(wball_pre, new Vector3(posx,posy,posz), wball_pre.transform.rotation);
        }














public Rigidbody white;
    public float posx;
    public float posy;
    public float posz;
    public float rotx;
    public float roty;
    public float rotz;
    public bool res;

    res = false;


if(stick.isfired == true){
                stick.isfired = false;
                print("Ball stopped moving");
                //posx = whole_stick.transform.position.x;
                //posy = whole_stick.transform.position.y;
                //posz = whole_stick.transform.position.z;
                

                //Instantiate(whole_stick, new Vector3(posx,posy,posz), Quaternion.identity);

            }












            if(white_ball.velocity==Vector3.zero){
            if(GameObject.FindGameObjectsWithTag("stick").Length <= 0){
               if(res == false){
                   print("Ball stopped moving"); 
                   
                   posx = white.transform.position.x;
                   posy =white.transform.position.y;
                   posz =white.transform.position.z;
                   rotx =white.transform.rotation.x;
                   roty =white.transform.rotation.y;
                   rotz =white.transform.rotation.z;
                   Destroy(white);
                   Destroy(white_ball);
                   Instantiate(white_ball, new Vector3(posx,posy,posz), Quaternion.Euler(new Vector3(rotx,roty,rotz)));
                   white_ball.isKinematic = true;
                   //Instantiate(white_ball, new Vector3(15.95999f, 11.59f, 3.87f), Quaternion.Euler(new Vector3(17.35f, 19.53f, 0)));
                   res = true;
               }
            //res = false;
            }
            
        }
        else{
            print("Ball MOVING");
        }
*/