#include <iostream>
using namespace std;

typedef long long ent;

ent powermod(ent a, ent b, ent m) {
  ent res;
  if (b==0) return 1;
  else if (b==1) return a;
  else if (b%2==0) {
    res = powermod(a,b/2,m);
    return (res*res)%m;
  }
  else {
    res = powermod(a,b/2,m);
    return (a*((res*res)%m))%m;
  }
}

int main() {
  ent b,p,m;
  while (cin >> b >> p >> m) {
    cout << powermod(b,p,m) << '\n';
  }
  return 0;
}
