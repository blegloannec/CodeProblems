#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;

const ent P1 = 10007;
const ent P2 = 30011;
const ent P3 = 50021;
const ent B1 = 29;
const ent B2 = 31;
const ent B3 = 37;

int N;
string S;
vector<ent> H1,H2,H3,H4,Bpow1,Bpow2,Bpow3,Bpow4;

void init_hash() {
  N = S.size();
  H1.resize(N+1,0);
  H2.resize(N+1,0);
  H3.resize(N+1,0);
  Bpow1.resize(N+1,1);
  Bpow2.resize(N+1,1);
  Bpow3.resize(N+1,1);
  for (int i=0; i<N; ++i) {
    ent c = S[i]-'a'+1;
    H1[i+1] = (((B1*H1[i])%P1) + c) % P1;
    H2[i+1] = (((B2*H2[i])%P2) + c) % P2;
    H3[i+1] = (((B3*H3[i])%P3) + c) % P3;
    Bpow1[i+1] = (Bpow1[i]*B1) % P1;
    Bpow2[i+1] = (Bpow2[i]*B2) % P2;
    Bpow3[i+1] = (Bpow3[i]*B3) % P3;
  }
}

ent get_hash(int L, int R) {
  ent h1 = (((H1[R] - ((H1[L]*Bpow1[R-L])%P1)) % P1) + P1) % P1;
  ent h2 = (((H2[R] - ((H2[L]*Bpow2[R-L])%P2)) % P2) + P2) % P2;
  ent h3 = (((H3[R] - ((H3[L]*Bpow3[R-L])%P3)) % P3) + P3) % P3;
  return h1 | (h2<<16) | (h3<<32);
}

int main() {
  cin >> S;
  init_hash();
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    int L,R;
    cin >> L >> R;
    cout << get_hash(L,R) << endl;
  }
  return 0;
}
