#include <iostream>
#include <math.h>

using namespace std;

bool is_sqrt(int n){
  int i=sqrt(n);
  return (i*i==n);
}

int change_base(int n, int b){
  int res=0;
  int aux=1;
  while (n!=0){
    if (n%10>=b)
      return 3;
    res+= aux* (n%10);
    n=n/10;
    aux*= b;
  }
  return res;
}

int aux(int n){
  for (int i=2;i<101;i++)
    if (is_sqrt(change_base(n,i)))
      return i;
  return -1;
}

int main(){
  int n;
  cin >> n;
  while (n){
    cout << aux(n) << '\n';
    cin >> n;
  }
}
