#include <iostream>
using namespace std;

int A,B,C;

bool tribo(int p) {
  int a0 = A%p, b0 = B%p, c0 = C%p;
  if (a0==0 || b0==0 || c0==0) return false;
  int a = a0, b = b0, c = c0;
  int d = (a+b+c) % p;
  a = b; b = c; c = d;
  while (c!=0 && !(a==a0 && b==b0 && c==c0)) {
    d = a+b+c;
    while (d>=p) d -= p;  // faster than %
    a = b; b = c; c = d;
  }
  return c!=0;
}

int main() {
  int K;
  cin >> A >> B >> C >> K;
  int p = 3, cpt = 0;
  while (cpt<K) {
    if (tribo(p)) ++cpt;
    p += 2;
  }
  cout << p-2 << endl;
  return 0;
}
