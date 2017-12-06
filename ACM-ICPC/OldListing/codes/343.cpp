#include <iostream>
using namespace std;

typedef long long ent;

ent a[37];
ent b[37];

ent cconv(char c) {
  if (c-'0' < 10) return c-'0';
  else return c-'A'+10;
}

ent conv(string s, int b) {
  ent res = 0;
  for (int i=0; i<(int)s.length(); ++i) {
    if (cconv(s[i])>=b || cconv(s[i])<0) return -1;
    if (b==1) ++res;
    else res = b*res + cconv(s[i]);
  }
  return res;
}

int main() {
  string s,t;
  int ia,ib;
  while (cin >> s >> t) {
    for (int i=1; i<37; ++i) {
      a[i] = conv(s,i);
      b[i] = conv(t,i);
    }
    /* //cas base 1
       if (a[1]!=-1 && b[1]!=-1) {
      if (a[1]==b[1]) cout << s << " (base 1) = " << t << " (base 1)\n";
      else cout << s << " (base 2) = " << t << " (base 2)\n";
      continue;
      }*/
    ia = ib = 2;
    while (ia<37 && ib<37 && !(a[ia]==b[ib] && a[ia]!=-1)) {
      if (a[ia]<b[ib] && ia<36) ++ia;
      else ++ib;
    }
    if (ia<37 && ib<37) 
      cout << s << " (base " << ia << ") = " << t << " (base " << ib << ")\n";
    else cout << s << " is not equal to " << t << " in any base 2..36\n";
  }
  return 0;
}
