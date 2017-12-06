#include <iostream>

using namespace std;

#define NMAX 4000000

int counttab[NMAX];

int art(int a, int b){
  int c = 1, aux = a;
  while (b%aux==0){
    c++;
    aux = aux*a;
  }
  return c-1;
}

void init(){
  int aux=2;
  while (aux<NMAX){
    counttab[aux]= counttab[aux] + (art(2, aux));
    aux = aux +2;
  }
  for (int i=3;i<=NMAX-1;i=i+2){
    if (counttab[i]==0){
      aux=i;
      while (aux<NMAX){
	counttab[aux]= counttab[aux] + (art(i, aux));
	aux = aux +i;
      }
    }
  }
}

int func(int n){
  int res=2, aux=0;
  while (aux<=n){
    aux = aux + counttab[res];
    res++;
  }
  return res-1;
}

int main(){
  int nb_cas, n;
  for (int i=0;i<NMAX;i++)
    counttab[i]=0;
  counttab[0]=1;
  counttab[1]=1;
  init();
  cin >> nb_cas;
  while (nb_cas-->0){
    cin >> n;
    cout << func(n) << '\n';
  }
  return 0;
}
