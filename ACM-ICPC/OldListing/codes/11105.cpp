#include <iostream>
#include <algorithm>
#define MAX 250001
using namespace std;
int cribble[MAX];
int primes[MAX];
int point_pr;
bool prime[MAX];
bool bon[MAX];
int somme_bon[MAX];

void avance(){
  point_pr = -1;
  prime[1] = true;
  for(int i = 1; i < MAX; ++i){
    prime[i] = true;
  }
  for(int i = 1; i < MAX; ++i){
    if(prime[i]){
      point_pr++;
      primes[point_pr] = i;
      int add = 4*(4*i+1);
      int j = 4*i+1;
      while(j < MAX){
	j = j+add;
	prime[(j-1)/4] = false;
      }
    }
  }
}


int main(void){
  avance();
  for(int i = 0; i < point_pr; ++i){
    bon[i] = false;
  }
  for(int i = 0; i < point_pr; ++i){
    for(int j= 0; j <= i; ++j){
      int prod = (((4*primes[i]+1) * (4*primes[j]+1))-1) / 4;
      if(prod < MAX) 
	{
	  //cout << "bon " << prod << endl;
	  bon[prod] = true; 
	}
      else break;
    }
  }
  int somme = 0;
  for(int i = 0; i < MAX; ++i){
    if(bon[i] == true){
      somme++;
    }
    somme_bon[i] = somme;
    //cout << "somme " << somme << endl;
  }
  
  /*for(int i = 0; i < 200; ++i){
    cout << bon[i] << " " ; //"-" << somme_bon[i] << " ";

    }*/

  int t;
  while(cin >> t){
    if (t == 0) return 0;
    cout << t << " " << somme_bon[(t-1)/4] << endl;
  }

  return 0;

}
