#include <iostream>
#include <cmath>
using namespace std;

int prime[100000001];

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

int main() {
  int n;
  prime[1] = 0; 
  prime[2] = 1;
  for (int i=3; i<=100000000; i++)
    prime[i] = -1;
  bool found;
  while (cin >> n) {
    if (n==0) return 0;
    if (isprime(n-2)) {
      cout << n << ":\n2+" << n-2 << '\n';
    }
    else {
      found = false;
      for (int k=3; k<=n/2; k+=2)
	if (isprime(k)&&isprime(n-k)) {
	  found = true;
	  cout << n << ":\n" << k << '+' << n-k << '\n';
	  break;
	}
      if (!found) cout << n << ":\nNO WAY!\n";
    }
  }
  return 0;
}
