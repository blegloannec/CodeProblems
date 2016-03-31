#include <iostream>
#include <cmath>
using namespace std;

int prime[1000001];

bool isprime(int n) {
  if (prime[n]>=0) {
    if (prime[n]>0) return true;
    return false;
  }
  if (n%2==0) return false;
  int r = (int)floor(sqrt(n));
  for (int k=3; k<=r; k+=2)
    if (n%k==0) {
      prime[n] = 0;
      return false;
    }
  prime[n] = 1;
  return true;
}

void counting(int n){
  for (int i=2;i<=n/2;i++){
    if (isprime(i) && isprime(n-i)){
      cout << i << " + " << (n-i);
      return;}
  }
}

int main(){
  int n;
  prime[1] = 0;
  prime[2] = 1;
  for (int i=3; i<=1000000; i++)
    prime[i] = -1;
  cin >> n;
  while (n!=0){
    cout << n << " = ";
    counting(n);
    cout << '\n';
    cin >> n;
  }
  return 0;
}
