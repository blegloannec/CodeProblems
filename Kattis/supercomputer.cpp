#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

/*
  Fenwick Trees
  /!\ indices (parameters i,a,b) are 1-based
      add ++i at the beginning of add/prefix_sum to change to 0-based
*/
typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  ent operator[](int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

ent Fenwick::operator[](int i) const {
  return prefix_sum(i)-prefix_sum(i-1);
}


int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int N,Q;
  cin >> N >> Q;
  Fenwick F(N);
  for (int q=0; q<Q; ++q) {
    char c;
    cin >> c;
    if (c=='F') {
      int i;
      cin >> i;
      F.add(i, (F[i] ? -1 : 1));
    }
    else {
      int l,r;
      cin >> l >> r;
      cout << F.prefix_sum(r)-F.prefix_sum(l-1) << '\n';
    }
  }
  return 0;
}
