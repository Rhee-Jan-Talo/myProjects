using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rotatestick : MonoBehaviour{
    Vector3 tempPos;
    //public Rigidbody rb;
    // Initialization
    //public static string s;
    
    void Start()
    {
        //rb = GetComponent<Rigidbody>();
        //s = "Yes";
    }

    // Update is called once per frame
    void Update(){
        if (Input.GetKey("w")){
            transform.Rotate(0.2f,0,0);
        }
        if (Input.GetKey("s")){
            transform.Rotate(-0.07f,0,0);
        }
        if (Input.GetKey("a")){
            transform.Rotate(0.2f,1,0);
        }
        if (Input.GetKey("d")){
            transform.Rotate(0,-0.2f,0);
        } 
        /*
        stick.posx = transform.position.x; //i set nmo ang position sa imong i-duplicate based sa posistion sa object where gi butang ni na script
        stick.posy = transform.position.y;
        stick.posz = transform.position.z;
        */
        //if(rb.velocity==Vector3.zero){
        //    print("Ball stopped moving");
        //}
        //else{
        //    print("Ball is moving");
        //}
    }
}
