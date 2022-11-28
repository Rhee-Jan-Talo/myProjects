using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class removeimg : MonoBehaviour
{
    public Image img;
    public Image img2;
    
    void Start(){
        if(gameObject.name=="ball yellow"){
            img2 = GameObject.Find("IMG-ball1").GetComponent<Image>();
        }
        if(gameObject.name=="ball blue"){
            img2 = GameObject.Find("IMG-ball2").GetComponent<Image>();
        }
        if(gameObject.name=="ball red"){
            img2 = GameObject.Find("IMG-ball3").GetComponent<Image>();
        }
        if(gameObject.name=="ball pink"){
            img2 = GameObject.Find("IMG-ball4").GetComponent<Image>();
        }
        if(gameObject.name=="ball orange"){
            img2 = GameObject.Find("IMG-ball5").GetComponent<Image>();
        }
        if(gameObject.name=="ball green"){
            img2 = GameObject.Find("IMG-ball6").GetComponent<Image>();
        }
        if(gameObject.name=="ball violet"){
            img2 = GameObject.Find("IMG-ball7").GetComponent<Image>();
        }
        if(gameObject.name=="ball black"){
            img2 = GameObject.Find("IMG-ball8").GetComponent<Image>();
        }
        if(gameObject.name=="ball yellow_d"){
            img2 = GameObject.Find("IMG-ball9").GetComponent<Image>();
        }

    }
    void Update(){
        if(GameObject.FindGameObjectsWithTag("red ball").Length == 9){
            img.enabled = true;
        }
        print(gameObject.tag.GetType());
    }
    void OnDestroy(){
        //img.enabled = false;
        img2.enabled = false;
    }
}
