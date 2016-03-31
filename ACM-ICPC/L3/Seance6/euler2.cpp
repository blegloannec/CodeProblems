#include <iostream>
#include <cmath>
using namespace std;


int ind_euler(int n) {
  if (n==1) return 0;
  int k = n;
  int c = 0;
  int res = 1;
  while (k%2==0) {
    k = k/2;
    c++;
  }
  if (c>0) res *= (int)pow(2,(double)(c-1));

  int s = (int)floor(sqrt(n));
  int p = 3;
  while ((k>1)&&(p<=s)) {
    c = 0;
    while (k%p==0) {
      k = k/p;
      c++;
    }
    if (c==1) {
      res *= p-1;
      s = (int)floor(sqrt(k));
    }
    else if (c>1) {
      res *= (p-1) * (int)pow((double)p,(double)(c-1));
      s = (int)floor(sqrt(k));
    }
    p += 2;
  }
  if (k>1) res *= k-1;
  return res;
}


int main() {
  int n;
 
  while (cin >> n) {
    if (n==0) return 0;
    cout << ind_euler(n) << endl;
  }
  
  return 0;
}
