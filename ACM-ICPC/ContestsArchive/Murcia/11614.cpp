#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int cas;
  long long n;
  cin >> cas;
  
  while (cas-->0) {
    cin >> n;
    cout << (int)(floor((1+sqrt(1+8*n))/2))-1 << endl;
  }
  
  return 0;
}
