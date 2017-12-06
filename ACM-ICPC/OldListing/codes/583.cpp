#include <iostream>
#include <math.h>

using namespace std;

#define NMAX 47000

bool prime[NMAX];

void init(){

  for (int i=0;i<NMAX;i++)
    prime[i]=true;

  int aux=2;
  while (aux<NMAX-3){
    aux = aux +2;
    prime[aux]= false;
  }
  for (int i=3;i<NMAX;i=i+2){
    if (prime[i]){
      aux=i;
      while (aux<NMAX-i-1){
	aux = aux +i;
	prime[aux]= false;
      }
    }
  }
}


void decom(int n, bool t, int d){

  if (n==1)
    return;

  if (n<0){
    cout << "-1";
    return decom(-n, false, d);
      }

  if ((n%2)==0){
    if (not t)
      cout << " x ";
    cout << "2";
    return decom(n/2, false, d);
  }

  int nn = sqrt(n);

  for (int i=d;i<=nn+10;i=i+2){
    if (prime[i]){
      if ((n%i)==0){
	if (not t)
	  cout << " x ";
	cout << i;
	return decom(n/i, false, i);
      }
    }
  }
  if (not t)
    cout << " x ";
  cout << n;
    return;
}

int main(){
  int n;
  init();
  cin >> n;
  while (n!=0){
    cout << n << " = ";
    decom(n, true, 3);
    cout << '\n';
    cin >> n;
  }
  return 0;
}
