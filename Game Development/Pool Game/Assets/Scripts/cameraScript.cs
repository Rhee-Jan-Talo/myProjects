using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cameraScript : MonoBehaviour
{
    Vector3 tempPos;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
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
    }
}
