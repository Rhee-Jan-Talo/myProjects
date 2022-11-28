using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class stick : MonoBehaviour
{
    Vector3 tempPos;
    public static bool isfired ;
    public float force;
    public Rigidbody rb;
    public Rigidbody ball;
    public static GameObject obj; //declare a empty gameobject variable
    public Transform rot;
    public Vector3 forceapplied;
    public static GameObject stck ;
    public static float posx = 0f; // if mag declare kag float var
    public static float posy = 0f;
    public static float posz = 0f;

    void Start(){
        GetComponent<ConstantForce>().enabled=false;   
        rb = GetComponent<Rigidbody>();
        ball = GetComponent<Rigidbody>();
        obj = GetComponent<GameObject>();
        rb.isKinematic = true; 
        isfired = false;
    }

    // Update is called once per frame
    void Update(){
        //print(rotatestick.s);

        if(Input.GetButtonUp("Fire1")){
            rb.isKinematic=false;
            force = scrollBar.len * 1000;
            forceapplied = new Vector3(0, (scrollBar.len *-1)*1300, 0);
            GetComponent<ConstantForce>().enabled=true;
            rb.AddForce(Vector3.forward * force, ForceMode.Force);
            isfired = true;
        } 
        /*
        if(Input.GetButtonUp("Fire1")){
            rb.isKinematic=false;
            force = scrollBar.len *500  ;
            forceapplied = new Vector3(0, (scrollBar.len *-1)*1300, 0);
            GetComponent<ConstantForce>().enabled=true;
            rb.AddRelativeForce(forceapplied, ForceMode.Force);
            print(forceapplied);  
        } 
        */
        if(Input.GetKey("right")){
            tempPos = transform.position;
            //rb.useGravity = false;
            tempPos.x += 0.02f;
            transform.position=tempPos;
        }
        if(Input.GetKey("left")){
            tempPos = transform.position;
            tempPos.x -= 0.02f;
            transform.position=tempPos;
        }
        if(Input.GetKey("up")){
            tempPos = transform.position;
            tempPos.y += 0.02f;
            transform.position=tempPos;
        }
        if(Input.GetKey("down")){
            tempPos = transform.position;
            tempPos.y -= 0.02f;
            transform.position=tempPos;
        }
        /*
        if(rotatestick.s == "Yes"){ //destroy the current gameobject where this script is given
            Destroy(gameObject);
        }
        if(rotatestick.s == "Yes"){ //drag a gameobject a left panel na gsto nmo i-destroy
            Destroy(obj); //empty gameobject (magselect paka sa left panel)
        }
        Instantiate(obj, rot.position, rot.rotation);//select an object then duplicate it (object, desired position, desired rotation)
        
        Instantiate(gameObject, gameObject.transform.position, gameObject.transform.rotation); //duplicate the gameobject where this script is placed
        */
        //Instantiate(gameObject, new Vector3(posx, posy, posz), Quaternion.identity); //kani if i-declare nmo asa na position nmo want i butang ang gi duplicate (quaternion means no rotation)
        
        
    }
    void OnCollisionEnter(Collision other){
        //gameObject.SetActive(false);
        Destroy(gameObject);
    }
}
