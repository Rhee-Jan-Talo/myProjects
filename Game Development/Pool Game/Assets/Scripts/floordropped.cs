using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class floordropped : MonoBehaviour
{
    public GameObject wball;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void OnCollisionEnter(Collision collision){ //DLI NA NEED I SET TO TRIGGER ANG OBJECT
        if(collision.gameObject.tag=="white ball"){
            print("White ball dropped on the floor");
            Destroy(collision.gameObject);
            Instantiate(wball, new Vector3(15.95999f, 11.59f, 3.87f), Quaternion.Euler(new Vector3(17.35f, 19.53f, 0)));

        }
    }   
}
