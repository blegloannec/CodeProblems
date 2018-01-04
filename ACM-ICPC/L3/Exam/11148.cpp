#include <iostream>
using namespace std;

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int main() {
  int n;
  cin >> n;
  string S;
  getline(cin,S);
  while (n--) {
    getline(cin,S);
    int p = 1, q = 1;
    int r = 0, a = 0, p0 = 0, q0 = 1;
    bool num = false, denom = false;
    for (unsigned int i=0; i<S.size(); ++i) {
      if ('0'<=S[i] && S[i]<='9') {
	r = 10*r + S[i]-'0';
	num = true;
      }
      else if (num) {
	if (S[i]=='-') a = r;
	else if (S[i]=='/') {
	  p0 = r;
	  denom = true;
	}
	else {
	  if (denom) q0 = r;
	  else p0 = r;
	  p *= a*q0+p0;
	  q *= q0;
	  a = 0; p0 = 0; q0 = 1;
	  denom = false;
	}
	r = 0;
	num = false;
      }
    }
    int g = gcd(p,q);
    p /= g; q /= g;
    a = p/q;
    if (a>0 && q>1) {
      cout << a << '-';
      p -= a*q;
    }
    cout << p;
    if (q>1) cout << '/' << q;
    cout << endl;
  }
  return 0;
}
