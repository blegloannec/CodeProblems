#include <iostream>
#include <cmath>
using namespace std;




bool is_prime(int n) {
  if (n%2==0) return false;
  for (int i=3; i<=sqrt(n); i+=2) 
    if (n%i==0) return false;
  return true;
}

int main() {
  int c = 1;
  cout << "int primes [] = {2";
  for (int i=3; i<=35000; i+=2) 
    if (is_prime(i)) { 
      cout << "," << i;
      c++;
    }
  cout << endl << c << endl;
  return 0;
}
