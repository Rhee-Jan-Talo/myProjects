using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class scrollBar : MonoBehaviour
{
    // Start is called before the first frame update
    public static float len;
    void Start()
    {
        transform.GetComponent<Scrollbar>().size = len; //butangi ug F pirmi pag float
        len = 0.0f;
    }

    // Update is called once per frame
    void Update()
    {

        len = len + 0.0009f;
        transform.GetComponent<Scrollbar>().size = len;
        if(len>=1){
            len=0.0f;
        }
        
    }
}
