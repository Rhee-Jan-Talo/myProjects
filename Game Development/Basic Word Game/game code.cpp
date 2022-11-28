#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <windows.h>
#include <cstdlib>
#include <ctime>
#include <MMsystem.h>
using namespace std;


void health(int hp, int hp2){
	cout<<"Your HP: "<<hp<<"         Enemy HP: "<<hp2;
	Sleep(1300);
	system("cls");
}

bool Battle1(bool t)
{
	t = false;
	int hp,hp2,h;
	PlaySound(TEXT("first battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---------Prepare for BATTLE!!---------";
	Sleep(1300);
	system("cls");
	hp = 5; hp2 = 3;
	health(hp,hp2);
	string word,word2;
    string words[] = {"int_number;","bool_Istrue;","string_name;","double_grade;","float_qpi;","bool_bol;","Clock_t_time;","long_dog;","string_mahalkosya;","string_crush;","string_lolo;","int_value;","bool_papasaba;","int_prefigrade;","string_subj;","long_stick;","float_mamal;","double_penet;","clock_t_finish;","clock_t_start;"};
    h = 1;
    while (h!= 0 ){
    	int i = rand() % 19;
    	word = words[i];
	    clock_t start = clock();	
		string ans;
		cout<<"Timer: 10 Seconds"<<endl;
		Sleep(1400);
	    system("cls");
		cout << "Type this line:		Timer : 10 seconds\n"<<"	"<<word<<endl;
		cin>>word2;
		clock_t finish = clock();
		system("cls");
		double time = (finish-start)/CLOCKS_PER_SEC;
		cout << "IT TOOK YOU " << time << " SECOND/s TO TYPE\n";
		Sleep(1300);
		system("cls");
			if (time<=10 && word2==word){	
				cout<<"YOU DEALT DAMAGE\nEnemy HP - 1"<<endl;
				hp2 = hp2 - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if (word2!= word){
				cout<<"INCORRECT INPUT \nATTACK FAIL :(\nYou lose 1 HP..."<<endl;	
				hp = hp-1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if ( time > 10){
				cout<< "YOU TYPED TOO SLOW\nATTACK FAIL :(\nYou lose 1 HP...";
				hp = hp - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
		if(hp == 0){
			h = 0;
			t = false;
		}
		if (hp2 == 0){
			h = 0;
			t = true;
		}
	}
	return t;	
}
bool Battle2(bool t)
{
	t = false;
	int hp,hp2,h;
	PlaySound(TEXT("first battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---------Prepare for BATTLE!!---------";
	Sleep(1300);
	system("cls");
	hp = 5; hp2 = 4;
	health(hp,hp2);
	string word,word2;
    string words[] = {"cin>>number;","cout<<Istrue;","cout<<name;","cout<<'A''';","getline(cin,ans);","cin>>lifepurpose;","getch();","getche();","cout <<'Got it';","cout<<'\n\n\n';","cin>>charmos;","cin>>ginamos;","cout<<raulgwapo;","cout<<raulbestteacher;","cout<<mahalkoprogramming;","cin>>love;","cout<<coutlang;","cin>>cout;","cout<<cin;"};
    h = 1;
    while (h!= 0 ){
    	int i = rand() % 19;
    	word = words[i];
	    clock_t start = clock();	
		string ans;
		cout<<"Timer: 8 Seconds"<<endl;
		Sleep(1300);
	    system("cls");
		cout << "Type this line:		Timer: 8 seconds\n"<<"	"<<word<<endl;
		cin>>word2;
		clock_t finish = clock();
		system("cls");
		double time = (finish-start)/CLOCKS_PER_SEC;
		cout << "IT TOOK YOU " << time << " SECOND/s TO TYPE\n";
		Sleep(1300);
		system("cls");
			if (time<=8 && word2==word){	
				cout<<"YOU DEALT DAMAGE\nEnemy HP - 1"<<endl;
				hp2 = hp2 - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if (word2!= word){
				cout<<"INCORRECT INPUT \nATTACK FAIL :(\nYou lose 1 HP..."<<endl;	
				hp = hp-1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if ( time > 8){
				cout<< "YOU TYPED TOO SLOW\nATTACK FAIL :(\nYou lose 1 HP...";
				hp = hp - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
		if(hp == 0){
			h = 0;
			t = false;
		}
		if (hp2 == 0){
			h = 0;
			t = true;
		}
	}
	return t;	
}
void ex(){
	exit(0);
	return;
}
bool Battle3(bool t)
{
	t = false;
	int hp,hp2,h;
	PlaySound(TEXT("first battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---------Prepare for BATTLE!!---------";
	Sleep(1300);
	system("cls");
	hp = 5; hp2 = 5;
	health(hp,hp2);
	string word,word2;
    string words[] = {"a=int(input())","def_gwapoko","random_randint","for_i_in_range(0,20)","print(bagsaknagrade)","a=[1,2,3,4]","from_Array_import_Array","map(array(list(print(a))))","array.extend(extend_array)","for_j_in_range(n,b)","print(a/b)","a='SANAPASADOAKO'","myArray[0]='Bill'","s=len(my_array)","func(int_var1)","arr.remove(element)","arr.insert()","a='pythondabest'","game.py","tru='gwaposiraul'"};
    h = 1;
    while (h!= 0 ){
    	int i = rand() % 19;
    	word = words[i];
	    clock_t start = clock();	
		string ans;
		cout<<"Timer: 7 Seconds"<<endl;
		Sleep(1300);
	    system("cls");
		cout << "Type this line: 		Timer: 7 seconds\n"<<"	"<<word<<endl;
		cin>>word2;
		clock_t finish = clock();
		system("cls");
		double time = (finish-start)/CLOCKS_PER_SEC;
		cout << "IT TOOK YOU " << time << " SECOND/s TO TYPE\n";
		Sleep(1300);
		system("cls");
			if (time<=7 && word2==word){	
				cout<<"YOU DEALT DAMAGE\nEnemy HP - 1"<<endl;
				hp2 = hp2 - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if (word2!= word){
				cout<<"INCORRECT INPUT \nATTACK FAIL :(\nYou lose 1 HP..."<<endl;	
				hp = hp-1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if ( time > 7){
				cout<< "YOU TYPED TOO SLOW\nATTACK FAIL :(\nYou lose 1 HP...";
				hp = hp - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
		if(hp == 0){
			h = 0;
			t = false;
		}
		if (hp2 == 0){
			h = 0;
			t = true;
		}
	}
	return t;
}
	
	
	
bool Battle4(bool t){
	t = false;
	int hp,hp2,h;
	PlaySound(TEXT("first battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---------Prepare for BATTLE!!---------";
	Sleep(1300);
	system("cls");
	hp = 5; hp2 = 6;
	health(hp,hp2);
	string word,word2;
    string words[] = {"01010110_10011010","10010100_11101011","11100001_00100101","01001010_11111001","01010101_11101001","00101101_11010010","01001011_11110000","10011011_10101011","11100101_101011101","10101100_11001100","10100100_11100010","01011011_10111111","11111111_00001000","00000101_11100110","11101010_00111000","0000011_10010010","00010101_00110000","00110101_110010111","01010101_10101010","00110011_11001100"};
    h = 1;
    while (h!= 0 ){
    	int i = rand() % 19;
    	word = words[i];
	    clock_t start = clock();	
		string ans;
		cout<<"Timer: 7 Seconds"<<endl;
		Sleep(1300);
	    system("cls");
		cout << "Type this line:		Timer: 7 seconds\n"<<"	"<<word<<endl;
		cin>>word2;
		clock_t finish = clock();
		system("cls");
		double time = (finish-start)/CLOCKS_PER_SEC;
		cout << "IT TOOK YOU " << time << " SECOND/s TO TYPE\n";
		Sleep(1300);
		system("cls");
			if (time<=7 && word2==word){	
				cout<<"YOU DEALT DAMAGE\nEnemy HP - 1"<<endl;
				hp2 = hp2 - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if (word2!= word){
				cout<<"INCORRECT INPUT \nATTACK FAIL :(\nYou lose 1 HP..."<<endl;	
				hp = hp-1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if ( time > 7){
				cout<< "YOU TYPED TOO SLOW\nATTACK FAIL :(\nYou lose 1 HP...";
				hp = hp - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
		if(hp == 0){
			h = 0;
			t = false;
		}
		if (hp2 == 0){
			h = 0;
			t = true;
		}
	}
	return t;	
}

bool Battle5(bool t)
{
	t = false;
	int hp,hp2,h;
	PlaySound(TEXT("first battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---------Prepare for BATTLE!!---------";
	Sleep(1300);
	system("cls");
	hp = 5; hp2 = 8;
	health(hp,hp2);
	string word,word2;
    string words[] = {"bool_Istrue;","myArray[0]='Bill'","s=len(my_array)","func(int_var1)","cout<<purposeinlife;","name=str(input())","string_raulgwapo;","00110101_110010111","01010101_10101010","00110011_11001100","Clock_t_time;","long_dog;","string_mahalkosya;","cout<<raulgwapo;","cout<<raulbestteacher;","cout<<mahalkoprogramming;"};
    h = 1;
    while (h!= 0 ){
    	int i = rand() % 19;
    	word = words[i];
	    clock_t start = clock();	
		string ans;
		cout<<"Timer: 6 Seconds"<<endl;
		Sleep(1300);
	    system("cls");
		cout << "Type this line:		Timer: 6 seconds\n"<<"	"<<word<<endl;
		cin>>word2;
		clock_t finish = clock();
		system("cls");
		double time = (finish-start)/CLOCKS_PER_SEC;
		cout << "IT TOOK YOU " << time << " SECOND/s TO TYPE\n";
		Sleep(1300);
		system("cls");
			if (time<=6 && word2==word){	
				cout<<"YOU DEALT DAMAGE\nEnemy HP - 1"<<endl;
				hp2 = hp2 - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if (word2!= word){
				cout<<"INCORRECT INPUT \nATTACK FAIL :(\nYou lose 1 HP..."<<endl;	
				hp = hp-1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
			else if ( time > 6){
				cout<< "YOU TYPED TOO SLOW\nATTACK FAIL :(\nYou lose 1 HP...";
				hp = hp - 1;
				Sleep(2000);
				system("cls");
				health(hp,hp2);
			}
		if(hp == 0){
			h = 0;
			t = false;
		}
		if (hp2 == 0){
			h = 0;
			t = true;
		}
	}
	return t;	
}



void result(bool t){
		if (t == true)
			cout<<"YOU WIN!!";
		else
		{
				
			cout<<"YOU LOSE :((";
			ex();
		}
			
		Sleep(1300);
		system("cls");
		
		return;
	
}

void endgame(){
	PlaySound(TEXT("goodbye.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"MADE BY: Rhee Jan A. Talo, Bs - Information Systems \nThanks for Playing :>> :))" <<endl<<endl<<endl;
	system("pause");
	ex();
	return;
}
void instruction(){
	int a;
	cout<<"How to play: \n\n\n1.) Type a list of words // numbers // phrases // lines of codes within a particular time.\n2.) The enemy loses one (1) HP for every successful attempt.\n3.) The goal is to turn your enemy's health into zero (0) without letting your health reach zero (0).\n4.) HAVE FUN!!\n\n\n";
	cout<<"PROCCED TO GAME? .. \nPRESS 0 TO START GAME.\n";
	cin>>a;
return;
}

void menu(){
	string ans;
	PlaySound(TEXT("intro ending.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"^v^v^v^v^v^V^V^v^v^v^v^v^v^V^V^v^v^v^v^v^v^V^V^v^v^v^v^v^v^V^V^v^v^v^v^v^v^V\n";
	cout<<">                                                                          <"<<endl;
	cout<<"<                                                                          >"<<endl;
	cout<<"<                             0 1 0 1 1 0 0 1                              >"<<endl;
	cout<<"<                             0 1 1 0 1 1 1 1                              >"<<endl;
	cout<<">                             0 1 1 1 0 1 0 1                              <"<<endl;
	cout<<"<                             0 0 0 0 1 0 1 0                              >"<<endl;
	cout<<">                                                                          <"<<endl;
	cout<<">                                                                          <"<<endl;
	cout<<"<  Press 0 to start                                                        >"<<endl;
	cout<<">  Press 1 for Instructions                                                <"<<endl;
	cout<<"<  Press 2 to Exit                                                         >"<<endl;
	cout<<"^v^v^v^v^v^V^V^v^v^v^v^v^v^V^V^v^v^v^v^v^v^V^V^v^v^v^v^v^v^V^V^v^v^v^v^v^v^V"<<endl;
	cin>>ans;
	system("cls");
	if (ans == "0")
		return;
	else if(ans == "1")
		instruction();
	else if (ans == "2")
		endgame();

	else{
		cout<<"INCORRECT INPUT\nGAME CRASHED";
		ex();
	}
		
	return;
	
	
}
	

int main (){
	bool t = false;
	bool t2 = false;
	bool t3 = false;
	bool t4 = false;
	bool t5 = false;
	int hp,hp2;
	string name;
	menu();
	system("cls");
	cout<<"Enter your name: ";
	cin>>name;
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	PlaySound(TEXT("intro ending.wav") ,NULL, SND_LOOP|SND_ASYNC);
	system("cls");
	cout<< "*2:55 AM...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<< "*2/100 test cases passed...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Ugh annoying mani ni na program oy dili mugana :< (sigh)...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": KATULOGON NAKOO...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<< "*You fought your eyes to stay awake...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Gana na baaa.. i've been up all night na gudd'...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": PATULOGA NA KOOO...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Pleaseeee workkkk...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<< "*Eyes slowly closing...*\n\n\n\n\n\n\n\n\n\n";
	Sleep(800);
	system("cls");
	cout<<"*You fell asleep*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	system("cls");
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"*There's a distant voice, an awakening cry...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*The programming universe has awaken you...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Welcome to the digital universe of programming "<<name<<"!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": LUHH?(confused scream) unsa manii?...)\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Only you can find the answer that...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*The road you must travel will present tests and trials...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Five Gods...*\n\n\n\n\n\n\n\n\n\n";
	Sleep(800);
	system("cls");
	cout<<"One Treasure...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Accept the challenge and find your way out...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*With patience and faith, the missing pieces will fit...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	system("cls");
	cout<<"---Chapter 0: Variable | One Man's Constant---\n\n\n\n\n\n\n\n\n\n"; 
	system("pause");
	system("cls");
	cout<<"*Paasa the God of Variable awakens...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Paasa: Who dare awakens me?!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Help! I just want to find my way out...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Paasa: Are you worthy?\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Uhm... YES!! I AM WORTHY hehe...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Paasa: Challenge me. The man beneath the blank canvas.\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	t = Battle1(t);
	result(t);
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"Paasa: A brave soul.. Impressive...\n\n\n\n\n\n\n\n\n\n"; 
	system("pause");
	system("cls");
	cout<<name<<": hehe i won... so how do I get out of here?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Paasa: Bring this. Maybe a friend of mine could help...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You received [#include!]*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Paasa: It's the key to the next door. May the Gods guide your lost soul.\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Oki...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"CHAPTER 0 ---- COMPLETED!!!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	system("cls");
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---Chapter 1: Header Function | The Functionality of Abstraction---\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*A huge tombstone appeared...*\n\n\n\n\n\n\n\n\n\n"; 
	system("pause");
	system("cls");
	cout<<"*'<iostream>' it says...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You placed [#include] in the tombstone...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You are blinded by an unknown light...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*As you open your eyes.. A figure of a man appeared...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Uhm... hello... I'm looking for Paasa's friend.\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Patrick never mentioned a visitor. What brings you here?*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": I want to... uhm... get out of this universe.. cuz... I don't belong here..\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*What makes you think I'd help you?*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": btw... who are you?\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*I give meaning to cin, cout, cerr, and many more.\n Without me, they are nothing. I am Stony, the God of Iostream.*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": How do I get out of here? What do you want?\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Stony: You gotta fight for what you want, lost soul...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	t2 = Battle2(t2);
	result(t2);
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	system("pause");
	system("cls");
	cout<<"Stony: Tsk.. I underestimated you...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": hehe... so how do I get out of here? Tell me this instant.\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Stony: You gotta learn, brave soul.. It's the only way out..\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"CHAPTER 1 ---- COMPLETED!!!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	system("cls");
	cout<<"---Chapter 2: A Python's Story | The Multi-paradigm Programming Language---\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Hiss...\n\n\n\n\n\n\n\n\n\n"; 
	system("pause");
	system("cls");
	cout<<"*The sound of a creature circulates around you...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*I'm hungry.. Hiss.. Has my food arrived?...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Uhm... Hello?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Hiss.. An intruder!!!*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Wait!!!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	t3 = Battle3(t3);
	result(t3);	
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"*Who are you?! Hiss!? And why have you come here to my home?!*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Ayaw ko ng away! I just wanted to get out of this universe!...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*I see.. Hiss.. Another lost soul...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Will you be able to help me? >.<\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*The name's Oogs, the God of Python.. Hiss.. You're almost there!*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Huh??... What do you mean?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Oogs: You'll figure out yourself.. Hiss.. Bring this...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You received Binary Translator!*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"CHAPTER 2 ---- COMPLETED!!!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	system("cls");
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"---Chapter 3: 0130010 | 0130001 01101100 01101001---\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*0110300 01100101 01101100 01101100 01101111 00111111\n\n\n\n\n\n\n\n\n\n"; 
	system("pause");
	system("cls");
	cout<<name<<": Ha?...Hakdog?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*01101100 01101111 01110011 01110100 00111111*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": ...[confused]...ay tama diay\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You used Binary Translator!*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*I know what you're looking for, "<<name<<" ...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": naa raman diay na hahaha...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": So... how do you know me?\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*I've seen you grow through out the past Gods...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Who are you?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*The brain behind the coding system.. Aliño, the God of Binaries!...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Help! Tagal ko nang nakulong dito.. hmp!...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Aliño: I know.. And I'm here to help you...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Thank the Gods! Finally!...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Aliño: But you have to prove yourself first. Challenge my Demi-gods, 0 and 1 and show me you are worthy!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"0: Another lost soul? Easy hahahaha!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"1: Let's do this, brother!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	t4 = Battle4(t4);
	result(t4);
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"0: Grrr...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"1: Tsk...";
	system("pause");
	system("cls");
	cout<<"Aliño: Unbelievable! No one's ever defeated my Demi-gods except Raul...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<":hehe :>... now get me out of here!...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Aliño: You'll have your answers in no time, lost soul...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": I don't even know why I'm here!...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Aliño: Nobody knows why...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Aliño: It's all a matter of perspective.. You're ready.. Face him...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"CHAPTER 3 ---- COMPLETED!!!\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";
	Sleep(300);
	system("cls");
	cout<<".....";
	Sleep(300);
	system("cls");
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"Final Chapter: Coding | The Language of the Future\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*The Gods have told me your story.. I have been waiting...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": ..last nani boss?.. daghan pako SA na buhaton ba -_-\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Only you could answer those questions...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": HNG!!.. Who are you?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You've been through much. And I knew from the start that you could make it up until this moment...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You are the creator of your own destiny.. You chose your own path, " <<name<<"...\n\n\n\n\n\n\n\n\n\n*";
	system("pause");
	system("cls");
	cout<<name<<": ... awiee...Thanks! :>\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*This is your destiny...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Then what do I have to do?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*One last test, and you'll be able to understand everything...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Are you sure? last na dyud ni?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Yes.. Face me.. The God of Programming.. RAUL!*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	t5 = Battle5(t5);
	result(t5);
	PlaySound(TEXT("battle.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"Raul: I'm proud of you, "<<name<<"...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<name<<": Is this where it ends?...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"Raul: Not even close.. This is where the real journey begins...\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Courage play a huge role in life...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*As you know it will make you reach so far...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*So go out and have your say...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*Keep your head up.., your heart strong.., and then my dear...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You can never go wrong...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You saw a light then you followed it...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<".";
	Sleep(300);
	system("cls");
	cout<<"..";
	Sleep(300);
	system("cls");
	cout<<"...";
	Sleep(300);
	system("cls");
	cout<<"....";	
	Sleep(300);
	system("cls");
	cout<<".....";
	system("pause");
	system("cls");
	PlaySound(TEXT("intro ending.wav") ,NULL, SND_LOOP|SND_ASYNC);
	cout<<"*5:04AM...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You woke up...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*You look at your program...*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	cout<<"*---100/100 tests cases passed---*\n\n\n\n\n\n\n\n\n\n";
	system("pause");
	system("cls");
	endgame();
	
}
