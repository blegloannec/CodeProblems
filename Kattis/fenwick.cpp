#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

/* Fenwick Trees */
typedef long long ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

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


int main() {
  int N,Q;
  scanf("%d %d",&N,&Q);
  Fenwick F(N);
  for (int q=0; q<Q; ++q) {
    char c;
    int i;
    scanf(" %c %d",&c,&i);
    if (c=='+') {
      int d;
      scanf("%d",&d);
      F.add(i+1,d);
    }
    else printf("%lld\n",F.prefix_sum(i));
  }
  return 0;
}
