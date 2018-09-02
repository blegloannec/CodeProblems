#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;
int n,v1,v2,v3;
ent a,b,c;
vector< vector<int> > G;
vector<int> D,A(8);  // depth, mask to ancestor

int dfs(int u=0, int u0=-1) {
  int mask = 0;
  for (int i=1; i<=4; i<<=1)
    if (u==A[i]) mask |= i;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      D[*iv] = D[u]+1;
      mask |= dfs(*iv,u);
    }
  if (mask>0 && A[mask]<0) A[mask] = u;
  return mask;
}

/* 
  the DFS identifies the reduced tree:

          0
	  |
         (7)
      ---------
      |       |
   (m1|m2)    |
    -----     |
    |   |     |
   m1   m2    m3

  then the optimal path falls down into one of
  the 3 cases below (with the associated formulas)
  (NB: the editorial suggests either Dijkstra in the
       configurations graph of size 6^3, or a brute-force
       enumeration of all the possible paths in the
       reduced tree of size 6, instead of the formulas)
*/

ent path0(int m1, int m2, int m3) {
  // m1,m2 ~~ a ~~> m1|m2 ~~ b ~~> 7
  // either m3 ~~ a ~~> 7
  // or  m1&m2 ~~ b ~~> m3 ~~ c ~~> 7
  // m1&m2&m3 ~~ c ~~> 0
  return
    a * (D[A[m1]]-D[A[m1|m2]] + D[A[m2]]-D[A[m1|m2]]) +
    b * (D[A[m1|m2]]-D[A[7]]) +
    min(a,b+c) * (D[A[m3]]-D[A[7]]) +
    c * D[A[7]];
}

ent path1(int m1, int m2, int m3) {
  // m1,m3 ~~ a ~~> m1|m2
  // m1&m3 ~~ b ~~> m2
  // m1&m2&m3 ~~ c ~~> 0
  return
    a * (D[A[m1]]-D[A[m1|m2]] + D[A[m3]]-D[A[7]] + D[A[m1|m2]]-D[A[7]]) +
    b * (D[A[m2]]-D[A[m1|m2]]) +
    c * D[A[m2]];
}

ent path2(int m1, int m2, int m3) {
  // m1,m2,m3 ~~ a ~~> m1|m2
  // m1&m2&m3 ~~ c ~~> 0
  return
    a * (D[A[m1]]-D[A[m1|m2]] + D[A[m2]]-D[A[m1|m2]] + D[A[m3]]-D[A[7]] + D[A[m1|m2]]-D[A[7]]) +
    c * D[A[m1|m2]];
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> n;
    cin >> a >> b >> c;
    cin >> v1 >> v2 >> v3;
    --v1; --v2; --v3;
    G.resize(n);
    for (int i=0; i<n-1; ++i) {
      int u,v;
      cin >> u >> v; --u; --v;
      G[u].push_back(v);
      G[v].push_back(u);
    }
    // value modifications to simplify the formulas
    b = min(b,2*a);
    c = min(c,b+a);
    fill(A.begin(),A.end(),-1);
    int m1 = 1, m2 = 2, m3 = 4;
    A[m1] = v1; A[m2] = v2; A[m3] = v3;
    D.resize(n,0);
    dfs();
    for (int i=1; i<7; ++i)
      if (A[i]<0) A[i] = A[7];
    // swap if needed so that A[m1] and A[m2] have the deepest LCA
    if (A[m1|m3]!=A[7]) swap(m2,m3);
    else if (A[m2|m3]!=A[7]) swap(m1,m3);
    // formulas
    ent res = min(min(path0(m1,m2,m3),path2(m1,m2,m3)),min(path1(m1,m2,m3),path1(m2,m1,m3)));
    cout << res << endl;
    // cleaning
    G.clear();
    D.clear();
  }
  return 0;
}
