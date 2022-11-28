using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class moving : MonoBehaviour
{
    public Rigidbody rb;
    void Start()
    {
        rb=GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        if(rb.velocity==Vector3.zero){
            //print("Ball stopped moving");
        }
        else{
            //print("Ball is moving");
        }
    }
}
