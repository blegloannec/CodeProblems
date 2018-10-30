#include <cstdio>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cassert>
using namespace std;

int N,K,M;
vector<int> L,R,Time;
vector< pair<int,int> > TL;  // timeline
unordered_map<int,int> Idx;

/* Fenwick Trees */
typedef int ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;
  void range_add(int a, int b, ent v);

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

void Fenwick::range_add(int a, int b, ent v=1) {
  add(a,v);
  add(b+1,-v);
}

ent Fenwick::operator[](int i) const {
  return prefix_sum(i);
}
/* ===== */


int dicho(Fenwick &FT, int l0) {
  int l = l0, r = M;
  while (l<r) {
    int m = (l+r+1)/2;
    if (FT[m]<K) r = m-1;
    else l = m;
  }
  return l;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int cas=0; cas<T; ++cas) {
    scanf("%d %d",&N,&K);
    L.resize(N); R.resize(N);
    for (int i=0; i<N; ++i) {
      scanf("%d %d",&L[i],&R[i]);
      TL.push_back(make_pair(L[i],R[i]));
      TL.push_back(make_pair(R[i],-1));
    }
    // timeline et renumerotation/compression des bornes
    sort(TL.begin(),TL.end());
    M = 0;
    Time.resize(1);
    for (int i=0; i<(int)TL.size(); ++i)
      if (i==0 || TL[i].first!=TL[i-1].first) {
	Idx[TL[i].first] = ++M;
	Time.push_back(TL[i].first);
      }
    // approche O(n log^2 n)
    Fenwick FT(M);
    int i = 0, curr = 0, res = 0;
    while (i<(int)TL.size()) {
      int lt = TL[i].first, li = Idx[lt];
      while (i<(int)TL.size() && TL[i].first==lt){
	if (TL[i].second<0) --curr;
	else {
	  // on incremente l'intervalle [L[i],R[i]] dans le Fenwick
	  FT.range_add(li,Idx[TL[i].second],1);
	  ++curr;
	}
	++i;
      }
      /* curr contient le nb d'intervalles couvrant lt
	 et pour tout t>li, Ft[t] contient le nb d'intervalles
	 couvrant [lt,Time[t]], on cherche par dichotomie le 
	 plus grand t tel que FT[t]>=K */
      if (curr>=K) res = max(res,Time[dicho(FT,li)]-lt);
    }
    printf("%d\n",res);
    // cleaning
    TL.clear();
    Idx.clear();
  }
  return 0;
}
