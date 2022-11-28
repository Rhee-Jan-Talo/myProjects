using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class math : MonoBehaviour
{
    public TextMeshPro t1;
    public TextMeshPro t2;
    public TextMeshPro t3;
    public TextMeshPro t4;
    public TextMeshPro t5;

    public TextMeshPro ans1;
    public TextMeshPro ans2;
    public TextMeshPro ans3;
    public TextMeshPro ans4;
    public TextMeshPro ans5;
    public TextMeshPro ans6;
    public TextMeshPro ans7;
    public TextMeshPro ans8;

    public TextMeshPro finans1;
    public TextMeshPro finans2;
    public TextMeshPro finans3;
    public TextMeshPro finans4;
    public TextMeshPro finans5;
    public TextMeshPro finans6;



    int [] numbers = new int[5] {0,0,0,0,0};
    int [] ans = new int[8] {-1,-1,-1,-1,-1,-1,-1,-1};
    int [] finans = new int[6] {-1,-1,-1,-1,-1,-1};
    int j = 0;
    bool available = true;
    int carry=0;

    void Start()
    {
        
    }

    void Update()
    {   
        /*
        if(j<5){
            randomizer();
        }
        */
        numbers[0] = 1;
        numbers[1] = 1; 
        numbers[2] = 1; 
        numbers[3] = 2; 
        numbers[4] = 3;
        t1.SetText(numbers[0].ToString());
        t2.SetText(numbers[1].ToString());
        t3.SetText(numbers[2].ToString());
        t4.SetText(numbers[3].ToString());
        t5.SetText(numbers[4].ToString());
        /*
        t1.SetText(numbers[0].ToString());
        t2.SetText(numbers[1].ToString());
        t3.SetText(numbers[2].ToString());
        t4.SetText(numbers[3].ToString());
        t5.SetText(numbers[4].ToString());
        */
        solve();

    }
    public void randomizer(){
        available = false;
        
        int randint = Random.Range(1,9);
        for(int i=0; i<5; i++)
            {
            if(randint==numbers[i])
                {
                    available = true;
                }
            }
        if(available == false)
            {
                numbers[j] = randint;
                j++;
            }
            
        
    }
    public void solve(){
        ans[0] = numbers[0] * numbers[3];
        ans[1] =numbers[1] * numbers[3];
        ans[2] =numbers[2] * numbers[3];
        ans[3] =0;
        ans[4] =numbers[0] * numbers[4];
        ans[5] =numbers[1] * numbers[4];
        ans[6] =numbers[2] * numbers[4];
        ans[7] =0;
        addrows();

    }
    public void addrows(){
        if(ans[0]>=10){
            //ans[0]=1;
            //ans1.SetText(ans[0].ToString());
            carry=int.Parse(ans[0].ToString().Substring(0,1));
            ans1.SetText(ans[0].ToString().Substring(1,1));
            }else{
            ans1.SetText(ans[0].ToString());
            }  //display number

        if(ans[1]>=10){
            ans[1]=1;
            ans2.SetText(ans[1].ToString());
            }else{
            ans2.SetText(ans[1].ToString());
            }//display number

        if(ans[2]>=10){
            ans[2]=1;
            ans3.SetText(ans[2].ToString());
            }else{
            ans3.SetText(ans[2].ToString());
            }//display number

        if(ans[4]>=10){
            ans[4]=1;
            ans5.SetText(ans[4].ToString());
            }else{
            ans5.SetText(ans[4].ToString());
            }//display number

        if(ans[5]>=10){
            ans[5]=1;
            ans6.SetText(ans[5].ToString());
            }else{
            ans6.SetText(ans[5].ToString());
            }//display number

        if(ans[6]>=10){
            ans[6]=1;
            ans7.SetText(ans[6].ToString());
            }else{
            ans7.SetText(ans[6].ToString());
            }//display number

        ans4.SetText(ans[3].ToString());
        ans8.SetText(ans[7].ToString());
    }
}
