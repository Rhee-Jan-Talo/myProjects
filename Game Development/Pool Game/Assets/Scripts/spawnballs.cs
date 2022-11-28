using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class spawnballs : MonoBehaviour
{
    public Rigidbody yellowb;
    public Rigidbody blueb;
    public Rigidbody redb;
    public Rigidbody pinkb;
    public Rigidbody orangb;
    public Rigidbody greenb;
    public Rigidbody brownb;
    public Rigidbody blackb;
    public Rigidbody yellowd_b;
    public Image img1;
    public Image img2;
    public Image img3;
    public Image img4;
    public Image img5;
    public Image img6;
    public Image img7;
    public Image img8;
    public Image img9;
    

    //public float ballposx;
    //public float ballposy;
    //public float ballposz;

    //public Rigidbody all_balls;

    void Start()
    {
        //all_balls = GetComponent<Rigidbody>();
        //ballposx = yellowb.transform.position.x;
        //ballposy = yellowb.transform.position.y;
        //ballposz = yellowb.transform.position.z;
    }

    // Update is called once per frame
    void Update(){

    if(GameObject.FindGameObjectsWithTag("red ball").Length <= 0){ //if wala nay balls with tag="red ball"
        print("No mor balls");
        //Instantiate(all_balls, new Vector3(15.95999f, 33.42001f, 3.87f), Quaternion.identity);
        Instantiate(yellowb, new Vector3(15.88f, 11.58f, 11.73f), Quaternion.identity).name="ball yellow";   
        Instantiate(blueb, new Vector3(15.56f, 11.58f, 12.29f), Quaternion.identity).name="ball blue";   
        Instantiate(redb, new Vector3(16.23f, 11.58f, 12.28f), Quaternion.identity).name="ball red";   
        Instantiate(pinkb, new Vector3(15.21f, 11.58f, 12.86f), Quaternion.identity).name="ball pink";      
        Instantiate(orangb, new Vector3(15.88f, 11.58f, 12.85f), Quaternion.identity).name="ball orage";       
        Instantiate(greenb, new Vector3(16.57f, 11.58f, 12.88f), Quaternion.identity).name="ball green";       
        Instantiate(brownb, new Vector3(15.54f, 11.58f, 13.41f), Quaternion.identity).name="ball violet";        
        Instantiate(blackb, new Vector3(16.22f, 11.58f, 13.41f), Quaternion.identity).name="ball black";
        Instantiate(yellowd_b, new Vector3(15.87f, 11.58f, 13.93f), Quaternion.identity).name="ball yellow_d";
        yellowd_b.isKinematic = false;
        yellowb.isKinematic = false;
        blackb.isKinematic = false;
        brownb.isKinematic = false;
        greenb.isKinematic = false;
        orangb.isKinematic = false;
        pinkb.isKinematic = false;
        redb.isKinematic = false;
        blueb.isKinematic = false;  
        img1.enabled=true; 
        img2.enabled=true;  
        img3.enabled=true;  
        img4.enabled=true;   
        img5.enabled=true;  
        img6.enabled=true;  
        img7.enabled=true;  
        img8.enabled=true;  
        img9.enabled=true;  

        }
    }
}
