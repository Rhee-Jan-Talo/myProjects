using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class redball : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {   
        /*
        stick.posx = transform.position.x; //i set nmo ang position sa imong i-duplicate based sa posistion sa object where gi butang ni na script
        stick.posy = transform.position.y;
        stick.posz = transform.position.z;
        */
    }

    void OnCollisionEnter(Collision collision){ //DLI NA NEED I SET TO TRIGGER ANG OBJECT
        if(collision.gameObject.tag=="red ball"){
            //print("White ball Hit the red ball");
        }
        else if(collision.gameObject.tag=="edge"){
            //print("White ball Hit the edge");
        }
    }
}
