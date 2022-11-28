using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class balldropped : MonoBehaviour
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
        if(collision.gameObject.tag=="red ball"){
            print("A ball dropped");
            Destroy(collision.gameObject);
            //collision.gameObject.SetActive(false);
        }
        if(collision.gameObject.tag=="white ball"){
            print("White ball dropped");
            Destroy(collision.gameObject);

            Instantiate(wball, new Vector3(15.95999f, 11.59f, 3.87f), Quaternion.Euler(new Vector3(17.35f, 19.53f, 0)));
            //Instantiate(edge, new Vector3(posx2, posy2, posz2), Quaternion.identity); 
            //Instantiate(stickk, new Vector3(stickk.transform.position.x, stickk.transform.position.y, stickk.transform.position.z), Quaternion.Euler(stickk.transform.rotation.x,stickk.transform.rotation.y,stickk.transform.rotation.z)); 
        }
    }

}
