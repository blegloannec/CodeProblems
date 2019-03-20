#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ent = long long;


/* Fenwick Trees */
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
  ++i;  // 0-based --> 1-based
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ++i;  // 0-based --> 1-based
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
/* ===== */


int main() {
  int N;
  cin >> N;
  vector<ent> D(N);
  vector< pair<int,ent> > Dsorted;
  for (int i=0; i<N; ++i) {
    cin >> D[i];
    Dsorted.push_back(make_pair(D[i],i));
  }
  // compressing numbers and marking duplicates
  sort(Dsorted.begin(),Dsorted.end());
  vector<int> Duplicate(N,-1);
  int V = 0;
  for (int i=0; i<N; ++i) {
    if (i>0) {
      if (Dsorted[i].first!=Dsorted[i-1].first) ++V;
      else Duplicate[Dsorted[i].second] = Dsorted[i-1].second;
    }
    D[Dsorted[i].second] = V;
  }
  ++V;
  // counting lesser-anterior & greater-posterior values
  vector<ent> Before(N,0), After(N,0);
  Fenwick Fleft(V), Fright(V);
  for (int i=0; i<N; ++i) {
    if (Fleft[D[i]]==0)  // each value is only counted once
      Fleft.add(D[i]);
    if (D[i]>0) Before[i] = Fleft.prefix_sum(D[i]-1);
  }
  for (int i=N-1; i>=0; --i) {
    if (Fright[D[i]]==0) Fright.add(D[i]);
    if (D[i]<V) After[i] = Fright.prefix_sum(V-1) - Fright.prefix_sum(D[i]);
  }
  // gathering results
  ent res = 0;
  for (int i=0; i<N; ++i) {
    res += Before[i]*After[i];
    // if duplicate, remove common triplets
    if (Duplicate[i]>=0) res -= Before[Duplicate[i]]*After[i];
  }
  cout << res << endl;
  return 0;
}
