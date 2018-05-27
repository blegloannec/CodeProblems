/*
  The simple trick is to observe that, even though the maximum number of
  teams is N, the maximum number of different *sizes* of teams is O(sqrt(N)).
  Indeed to maximize the number K of different sizes of teams, take one team
  for increasing sizes 1+2+3+...+K = K*(K+1)/2 ~= N so that K = O(sqrt(N)).
  Hence each query can be dealt with in O(sqrt(N)) time by considering all
  the teams having the same size simultaneously.
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>
using namespace std;

/* Fenwick Trees */
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

// version classique
ent Fenwick::operator[](int i) const {
  return prefix_sum(i)-prefix_sum(i-1);
}

int N;
ent C;
vector<int> T,S;
unordered_map<int,int> G;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(Fenwick &F, int x, int y) {
  int x0 = find(x), y0 = find(y);
  if (x0!=y0) {
    --C;
    T[y0] = x0;
    F.add(S[x0],-1);
    F.add(S[y0],-1);
    --G[S[x0]];
    if (G[S[x0]]==0) G.erase(S[x0]);
    --G[S[y0]];
    if (G[S[y0]]==0) G.erase(S[y0]);
    S[x0] += S[y0];
    F.add(S[x0],1);
    ++G[S[x0]];
  }
}

int main() {
  int Q;
  cin >> N >> Q;
  C = N;
  T.resize(N,-1);
  S.resize(N,1);
  Fenwick F(N);
  F.add(1,N);
  G[1] = N;
  for (int q=0; q<Q; ++q) {
    int o;
    cin >> o;
    if (o==1) {
      int x,y;
      cin >> x >> y; --x; --y;
      merge(F,x,y);
    }
    else {
      int c;
      cin >> c;
      if (c==0) cout << C*(C-1)/2 << endl;
      else {
	ent res = 0;
	for (auto it=G.begin(); it!=G.end(); ++it) {
	  int s = it->first;
	  ent n = it->second;
	  if (s+c<=N) res += n*(F.prefix_sum(N)-F.prefix_sum(s+c-1));
	}
	cout << res << endl;
      }
    }
  }
  return 0;
}
