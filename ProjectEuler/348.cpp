#include <iostream>
#include <map>
using namespace std;

typedef long long ent;
typedef map<ent,int> assoc;

const int NMAX = 1000000000;

bool palindrome(ent n) {
  ent mirn = 0;
  ent nn = n;
  while (nn>0) {
    mirn = 10*mirn + nn%10;
    nn /= 10;
  }
  return mirn==n;
}

int main() {
  assoc cpt;
  for (ent a=1; a*a*a<NMAX; ++a) {
    ent a3 = a*a*a;
    for (ent b=1; a3+b*b<NMAX; ++b) {
      ent n = a3+b*b;
      if (palindrome(n)) ++cpt[n];
    }
  }
  ent S = 0;
  for (assoc::iterator it=cpt.begin(); it!=cpt.end(); ++it)
    if (it->second==4) {
      //cout << it->first << endl;
      S += it-> first;
    }
  cout << S << endl;
  return 0;
}
