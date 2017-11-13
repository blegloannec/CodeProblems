#include <cstdio>
#include <vector>
#include <map>
//#include <cassert>
using namespace std;

/*
  On maintient une liste triee des intervalles de valeurs consecutives <L
  (premier type) d'une part et <=R (second type) d'autre part.
  Tout sous-intervalle valide (L <= max <= R) est un sous-intervalle d'un
  intervalle du second type mais pas du premier type (et par definition
  les sous-intervalles du premier type sont aussi du second type).
  Le nb de sous-intervalles d'un intervalle de taille l est l(l+1)/2.
  La reponse a une requete [a,b] est la somme des nb de sous-intervalles
  sur les intervalles du second type inclus dans [a,b] a laquelle on
  soustrait la somme des nb de sous-intervalles sur les intervalles du premier
  type inclus dans [a,b].
  Chaque requete est traitee en O(log n) (recherche dicho aux 2 bords et
  Fenwick pour la somme des nb de sous-intervalles sur les intervalles
  strictement inclus).
*/

typedef long long ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  void set(int i, ent v);
  ent prefix_sum(int i) const;
  ent operator[](int i) const;

  Fenwick() {}
  
  Fenwick(int n) {
    FT.resize(n+1,0);
  }

  void resize(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  //assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

void Fenwick::set(int i, ent v) {
  //assert(i>0);
  add(i,v-(*this)[i]);
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


struct Intervals {
  int n;
  map<int,int> I;
  Fenwick F;

  Intervals(int N) {
    n = N;
    I[1] = n;
    F.resize(n);
    ent l = n;
    F.set(1,l*(l+1)/2);
  }

  void include(int x) {
    auto suiv = I.upper_bound(x);
    auto prev = suiv;
    bool has_suiv = (suiv!=I.end()), has_prev = (suiv!=I.begin());
    if (has_prev) --prev;
    if (has_prev && x<=prev->second) return; // element deja inclus
    if (has_prev && prev->second==x-1 && has_suiv && suiv->first==x+1) {
      I[prev->first] = suiv->second;
      ent l = suiv->second - prev->first + 1;
      F.set(prev->first,l*(l+1)/2);
      F.set(suiv->first,0);
      I.erase(suiv);
    }
    else if (has_prev && prev->second==x-1) {
      I[prev->first] = x;
      ent l = x - prev->first + 1;
      F.set(prev->first,l*(l+1)/2);
    }
    else if (has_suiv && suiv->first==x+1) {
      I[x] = suiv->second;
      ent l = suiv->second - x + 1;
      F.set(x,l*(l+1)/2);
      F.set(suiv->first,0);
      I.erase(suiv);
    }
    else {
      I[x] = x;
      F.set(x,1);
    }
  }

  void exclude(int x) {
    auto prev = I.upper_bound(x);
    if (prev==I.begin()) return; // element deja exclus
    --prev;
    if (prev->second<x) return;  // element deja exclus
    if (prev->second>x) {
      I[x+1] = prev->second;
      ent l = prev->second - (x+1) + 1;
      F.set(x+1,l*(l+1)/2);
    }
    if (prev->first==x) {
      F.set(prev->first,0);
      I.erase(prev);
    }
    else {
      I[prev->first] = x-1;
      ent l = x-1 - prev->first + 1;
      F.set(prev->first,l*(l+1)/2);
    }
  }
  
  void print() const {
    for (auto it=I.begin(); it!=I.end(); ++it)
      printf("%d-%d ",it->first,it->second);
    printf("\n");
  }

  ent range(int l, int r) {
    ent res = 0;
    auto prev = I.lower_bound(l);
    if (prev!=I.begin()) {
      --prev;
      if (l<=prev->second) {
	ent d = min(prev->second,r) - l + 1;
	res += d*(d+1)/2;
      }
    }
    auto suiv = I.upper_bound(r);
    if (suiv!=I.begin()) {
      --suiv;
      if (r<=suiv->second && l<=suiv->first) {
	ent d = r - suiv->first + 1;
	res += d*(d+1)/2 - F[suiv->first];
      }
    }
    res += F.prefix_sum(r)-F.prefix_sum(l-1);
    return res;
  }
};


int main() {
  int N,Q,L,R;
  scanf("%d %d %d %d",&N,&Q,&L,&R);
  vector<int> A(N+1,0);
  Intervals High(N),Low(N);
  for (int i=0; i<Q; ++i) {
    int c,x,y;
    scanf("%d %d %d",&c,&x,&y);
    if (c==1) {
      if (A[x]>=L && y<L) Low.include(x);
      else if (A[x]<L && y>=L) Low.exclude(x);
      if (A[x]>R && y<=R) High.include(x);
      else if (A[x]<=R && y>R) High.exclude(x);
      A[x] = y;
    }
    else {
      ent res = High.range(x,y) - Low.range(x,y);
      printf("%lld\n",res);
    }
  }
  return 0;
}
