#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

// === Fenwick Trees === //
typedef long long ent;

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
  ++i;
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ++i;
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
// ===== //


int N;
ent S;

ent diff(const Fenwick &F, int m) {
  ent L = m==0 ? 0 : F.prefix_sum(m-1);
  ent M = F.prefix_sum(m) - L;
  ent R = S-L-M;
  L += M/2;
  R += M/2;
  if (M%2==1) {
    if (L<R) ++L;
    else ++R;
  }
  return abs(R-L);
}

int dicho(const Fenwick &F) {
  int l = 0, r = N-1;
  while (l<r) {
    int ml = (l+r)/2;
    int mr = ml+1;
    ent dl = diff(F,ml), dr = diff(F,mr);
    if (dl<=dr) r = ml;
    else l = mr;
  }
  return l;
}

int main() {
  int Q;
  scanf("%d %d", &N, &Q);
  Fenwick F(N);
  for (int i=0; i<N; ++i) {
    ent a;
    scanf("%lld", &a);
    F.add(i,a);
    S += a;
  }
  for (int q=0; q<Q; ++q) {
    int i; ent x;
    scanf("%d %lld", &i, &x);
    x -= F[i];
    F.add(i,x);
    S += x;
    printf("%d\n", dicho(F));
  }
  return 0;
}
