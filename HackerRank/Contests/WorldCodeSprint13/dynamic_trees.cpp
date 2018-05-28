/*
  Could be solved using link/cut trees...
  But clever and way simpler sqrt decomposition approach here
  see editorial for details
  https://www.hackerrank.com/contests/world-codesprint-13/challenges/dynamic-trees/editorial
*/
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

int N,B,NB;
vector<int> Black,P,BBlack,BRoot;
vector<bool> seen;

void up_aux(int u) {
  if (!seen[u]) {
    seen[u] = true;
    if (P[u]<0 || P[u]/B!=u/B) { // P[u] est hors du bloc de u
      BRoot[u] = u;
      BBlack[u] = Black[u];
    }
    else {
      up_aux(P[u]);
      BRoot[u] = BRoot[P[u]];
      BBlack[u] = Black[u]+BBlack[P[u]];
    }
  }
}

void update_block(int b) {
  int L = b*B, R = min((b+1)*B,N);
  fill(seen.begin()+L,seen.begin()+R,false);
  for (int u=L; u<R; ++u)
    if (!seen[u]) up_aux(u);
}

int get_kth(int u, int k) {
  if (k==1 && Black[u]) return u;
  if (k-BBlack[u]>=1) return get_kth(P[BRoot[u]],k-BBlack[u]);
  return get_kth(P[u],k-Black[u]);
}

int climb_up(int u0, int v0, int k) {
  int u = u0, v = v0;
  int bu = 0, bv = 0;
  while (u/B!=v/B) {
    if (u>v) {
      bu += BBlack[u];
      u = P[BRoot[u]];
    }
    else {
      bv += BBlack[v];
      v = P[BRoot[v]];
    }
  }
  while (u!=v) {
    if (u>v) {
      bu += Black[u];
      u = P[u];
    }
    else {
      bv += Black[v];
      v = P[v];
    }
  }
  bu += Black[u];
  if (bu+bv<k) return -1;
  return k<=bu ? get_kth(u0,k) : get_kth(v0,bu+bv-k+1);
}

int main() {
  int Q;
  scanf("%d %d",&N,&Q);
  B = (int)sqrt(N)+1;
  NB = (N+B-1)/B;
  Black.resize(N);
  P.resize(N,-1);
  for (int i=0; i<N; ++i) scanf("%d",&Black[i]);
  for (int i=1; i<N; ++i) {
    int p;
    scanf("%d",&p); --p;
    P[i] = p;
  }
  seen.resize(N);
  BBlack.resize(N);
  BRoot.resize(N);
  for (int b=0; b<NB; ++b) update_block(b);
  for (int q=0; q<Q; ++q) {
    char c;
    scanf(" %c",&c);
    if (c=='T') {
      int x;
      scanf("%d",&x); --x;
      Black[x] = 1-Black[x];
      update_block(x/B);
    }
    else if (c=='C') {
      int u,v;
      scanf("%d %d",&u,&v); --u; --v;
      P[u] = v;
      update_block(u/B);
    }
    else {
      int u,v,k;
      scanf("%d %d %d",&u,&v,&k); --u; --v;
      int r = climb_up(u,v,k);
      if (r>=0) ++r;
      printf("%d\n",r);
    }
  }
  return 0;
}
