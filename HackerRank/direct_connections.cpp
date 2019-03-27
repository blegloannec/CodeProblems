/*
  O(N log N + N log P) approach, using sort (by position X) + Fenwick (by P)
  NB: The editorial proposes a kinda symmetric approach
      using sort by P + segment tree / Fenwick by X
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define _x_ first
#define _p_ second

typedef long long ent;
const ent MOD = 1000000007;

void add_mod(ent &a, ent b) {
  a = (a+b) % MOD;
}

ent mul(ent a, ent b) {
  return (a*b)%MOD;
}


/* == Fenwick Trees == */
struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix(int i) const;
  ent suffix(int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  //assert(i>0);
  while (i<(int)FT.size()) {
    add_mod(FT[i], v);
    i += i&-i;
  }
}

ent Fenwick::prefix(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    add_mod(s, FT[i]);
    i -= i&-i;
  }
  return s;
}

ent Fenwick::suffix(int i) const {
  return (prefix((int)FT.size()-1) - prefix(i) + MOD) % MOD;
}
/* ===== */


int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N;
    cin >> N;
    vector< pair<ent,int> > Cities(N);
    for (int i=0; i<N; ++i) cin >> Cities[i]._x_;
    int Pmax = 1;
    for (int i=0; i<N; ++i) {
      cin >> Cities[i]._p_;
      Pmax = max(Pmax, Cities[i]._p_);
    }
    sort(Cities.begin(),Cities.end());
    Fenwick FT_Cnt(Pmax), FT_X(Pmax), FT_P(Pmax), FT_XP(Pmax);
    ent res = 0;
    for (int i=0; i<N; ++i) {
      ent x = Cities[i]._x_;
      int p = Cities[i]._p_;
      // updating result linking city i to all cities j < i
      //   contributions of cities j < i such that Pj <= Pi
      add_mod(res, mul(mul(FT_Cnt.prefix(p),x) - FT_X.prefix(p) + MOD, p));
      //   contributions of cities j < i such that Pj > Pi
      add_mod(res, (mul(FT_P.suffix(p),x) - FT_XP.suffix(p) + MOD) % MOD);
      // update FTs including i-th city
      FT_Cnt.add(p, 1);
      FT_X.add(p, x);
      FT_P.add(p, p);
      FT_XP.add(p, (x*p)%MOD);
    }
    cout << res << endl;
  }
  return 0;
}
