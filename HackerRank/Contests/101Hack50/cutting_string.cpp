#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
  Forum post:
The editorial is nice and pretty clever. Yet there is a simpler (dumb and slower though) solution: a word w can be moved from position i to position j, say s = awb with w in position i and s = cwd with w in position j, iff ab = cd. For each factor size f, for each factor w of size f, compute its hash h1 and the hash h2 of s after cutting w (all this is done in O(1) if one has precomputed the hashes of the suffixes/prefixes of s) and count the couples (h1,h2) using a hashtable (for each considered factor size). If a couple is seen n times, then it adds n^2 to the final result. This O(|s|^2) approach passes if implemented efficiently (I had to try several modulus to pass without collision though).
*/

typedef unsigned long long ent;
typedef unordered_map<ent,int> dico;
const ent P = 4294900073;
const ent B = 26;

ent num(char c) {
  return (ent)c - (ent)'a';
}

inline void addmul(ent &c, ent a, ent b) {
  c += (a*b)%P;
  if (c>=P) c -= P;
}

int main() {
  string S;
  cin >> S;
  int n = S.size();
  vector<ent> s(n);
  for (int i=0; i<n; ++i) s[i] = num(S[i]);
  vector<ent> Bpow(n+1,1),HP(1,0),HS(1,0);
  for (int i=1; i<=n; ++i) Bpow[i] = (Bpow[i-1]*B)%P;
  ent h = 0;
  for (int i=0; i<n; ++i) {
    h = (((B*h)%P) + s[i]) % P;
    HP.push_back(h);
  }
  h = 0;
  for (int i=n-1; i>=0; --i) {
    h = (h + ((s[i]*Bpow[n-1-i])%P)) % P;
    HS.push_back(h);
  }
  ent comp;
  ent res = 0;
  dico D;
  for (int f=1; f<=n; ++f) {
    h = HP[f-1];
    for (int i=f-1; i<n; ++i) {
      //h = (B*h + s[i] - (((i-f>=0 ? s[i-f] : 0)*Bpow[f])%P)) % P;
      h = (h*B+s[i])%P;
      addmul(h,P-(i-f>=0 ? s[i-f] : 0),Bpow[f]);
      //comp = (((HP[i-f+1]*Bpow[n-i-1])%P) + HS[n-i-1]) % P;
      comp = HS[n-i-1];
      addmul(comp,HP[i-f+1],Bpow[n-i-1]);
      ++D[(h<<32) | comp];
    }
    for (dico::iterator x=D.begin(); x!=D.end(); ++x)
      res += (x->second)*(x->second);
    D.clear();
  }
  cout << res << endl;
  return 0;
}
