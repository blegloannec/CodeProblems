#include <iostream>
using namespace std;
using ll = long long;

const ll P = 1000000000000037LL;
const ll B = 11;

ll num(char c) {
  return (ll)c - (ll)'0';
}

int pal_dec(const string &S) {
  int i = 0, j = (int)S.size()-1, res = 0;
  ll hl = 0, hr = 0, Br = 1;
  while (i<j) {
    hl = (B*hl + num(S[i])) % P;
    hr = (hr + Br*num(S[j])) % P;
    if (hr==hl) {
      res += 2;
      hl = 0;
      hr = 0;
      Br = 1;
    }
    else Br = (B*Br) % P;
    ++i; --j;
  }
  if (Br>1 || i==j) ++res;
  return res;
}

int main() {
  string S;
  cin >> S;
  cout << pal_dec(S) << endl;
  return 0;
}
