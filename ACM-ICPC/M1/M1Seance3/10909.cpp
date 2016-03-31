#include <iostream>

using namespace std;

#define MAX 524288

int tab[3*MAX+5];
bool lucky[2*MAX+5];

void init(){
  int val=MAX;
  int nb=1;
  int k=1;
  while(val>=1){
    for (int i=0;i<nb;++i)
      tab[k++]=val;
    nb*=2;
    val/=2;
  }

  for (int i=2*MAX;i<3*MAX;++i)
    tab[i]=(i-2*MAX)*2+1;

  for (int i=0;i<2*MAX;++i)
    lucky[i]= (i%2==1);
}

int find(int k){
  //trouve le keme plus petit nombre
  int curr=1;
  while (curr<MAX){
    if (k<=tab[2*curr] && tab[2*curr]>0)
      curr= 2*curr;
    else{
      k= k-tab[2*curr];
      curr= 2*curr+1;
    }
  }
  return tab[curr+MAX];
}

void suppr(int k){
  //supprime le keme plus petit nombre
  int curr=1;
  while (curr<MAX){
    tab[curr]--;
    if (k<=tab[2*curr] && tab[2*curr]>0)
      curr= 2*curr;
    else{
      k= k-tab[2*curr];
      curr= 2*curr+1;
    }
  }
  tab[curr]--;
  lucky[tab[curr+MAX]]=false;
}

int main(){
  init();
  for (int k = 2; find(k) <= MAX; k++){
    int j= find(k)-1;
    for (int i = j+1; i < MAX && j>0; i += j)
      suppr(i);
  }

  int n, l1;
  while (cin >> n){
    if (n%2==1){
      cout << n << " is not the sum of two luckies!\n";
      continue;
    }
    l1= n/2;
    while (l1>0 && n-l1<2*MAX && !(lucky[l1]&&lucky[n-l1]))
      --l1;
    if (l1>0 && n-l1<2*MAX && (lucky[l1]&&lucky[n-l1]))
      cout << n << " is the sum of " << (l1) << " and " << (n-l1) << ".\n";
    else
      cout << n << " is not the sum of two luckies!\n";
  }

}
