#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;

typedef long long ent;

const ent P = 1000000007;

/* Fenwick Trees */
struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  // variante range
  void range_add(int a, int b, ent v);

  ent operator[](int i) const;

  Fenwick(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] = (FT[i]+v)%P;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s = (s+FT[i])%P;
    i -= i&-i;
  }
  return s;
}

void Fenwick::range_add(int a, int b, ent v=1) {
  add(a,v);
  add(b+1,P-v);
}

// variante range
ent Fenwick::operator[](int i) const {
  return prefix_sum(i);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int n,m;
    scanf("%d %d",&n,&m);
    vector<int> T(m+1),L(m+1),R(m+1);
    for (int i=1; i<=m; ++i)
      scanf("%d %d %d",&T[i],&L[i],&R[i]);
    // Premiere etape : on compte le nb total de fois que chaque commande
    // sera executee (directement ou indirectement), en parcourant les
    // commandes en sens inverse
    // O(m log m)
    Fenwick FTcom(m);
    for (int i=m; i>0; --i) {
      FTcom.range_add(i,i,1);
      if (T[i]==2) FTcom.range_add(L[i],R[i],FTcom[i]);
    }
    // Seconde etape : on calcule le tableau en appliquant les commandes
    // de type 1, connaissant le nb de fois qu'elles seront executees
    // O(n log n)
    Fenwick FTA(n+1);
    for (int i=1; i<=m; ++i)
      if (T[i]==1) FTA.range_add(L[i],R[i],FTcom[i]);
    for (int i=1; i<=n; ++i) {
      printf("%lld",FTA[i]);
      if (i<n) printf(" ");
      else printf("\n");
    }
  }
  return 0;
}
