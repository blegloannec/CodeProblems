#include <iostream>
#include <vector>
using namespace std;

string S0;
vector<int> R;

int manacher(string &S) {
  S0 = "^#";
  for (unsigned int i=0; i<S.size(); ++i) {
    S0 += S[i];
    S0 += '#';
  }
  S0 += '$';
  R.resize(S0.size(),0);
  int c = 0, d = 0, m = 0;
  for (int i=1; i<(int)S0.size()-1; ++i) {
    int j = 2*c-i; // miroir de i par rapport a c
    R[i] = max(0,min(R[j],d-i));
    while (S0[i+1+R[i]]==S0[i-1-R[i]]) ++R[i];
    if (i+R[i]>d) {
      c = i;
      d = i+R[i];
    }
    m = max(m,R[i]);
  }
  return m;
}

int main() {
  string S;
  cin >> S;
  int m = manacher(S);
  for (int i=1; i<(int)S0.size()-1; ++i)
    if (R[i]==m) cout << S.substr((i-m)/2,m) << endl;
  return 0;
}
