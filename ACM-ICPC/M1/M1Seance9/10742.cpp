#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

#define MAX 1000005

bool prime[MAX];
vector<int> premier;
int nombrepremier[MAX];


void eratosthene(int n){
  int m=sqrt(n);
  for(int i=0;i<n;i++)
    prime[i]= (i%2!=0);
  prime[1]=false;
  prime[2]=true;
  for(int i=3;i<=m;i+=2){
    if (prime[i])
      for(int j=2*i;j<n;j+=i)
	prime[j]=false;
  }
}

void primevect(int n){
  for (int i=0;i<n;++i)
    if (prime[i])
      premier.push_back(i);
}

void nbprem(int n){
  int nb=0;
  for(int i=0;i<n;++i){
    if (prime[i])
      nb++;
    nombrepremier[i]= nb;
  }
}

int compt(int n){
  int res=0;
  int i=0;
  int fprime= premier[0];
  while (fprime<= n/2){
    i++;
    res+= ((nombrepremier[n-fprime])-nombrepremier[fprime]);
    fprime= premier[i];
  }
  return res;
}

int main(){
  int n;
  int cas=0;
  int res=0;
  eratosthene(MAX);
  primevect(MAX);
  nbprem(MAX);

  cin >> n;
  while (n!=0){
    cout << "Case " << ++cas << ": " << compt(n) << "\n";
    cin >> n;
  }
}
