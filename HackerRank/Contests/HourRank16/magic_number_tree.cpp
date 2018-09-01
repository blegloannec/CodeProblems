#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
  "Medium" difficulty, yet pretty hard to find the right approach...
  Splitting E for vertices or edges do not work.
  We split it for paths.
  Consider the unique path between u and v and let d be the
  unitary (edge) distance and dw its weighted distance.
  There are d-1 intermediate vertices between u and v.
  The path counts into the score iff u or v is picked before any
  intermediate vertex.
  The number of corresponding permutations is:
  binom(n,d+1) * 2 * d! * (n-(d+1))!
  as we pick d+1 positions for vertices of the path
  you choose u or v to be first
  you choose a permutation for the d remaining vertices
  you choose a permutation for the rest of the tree
  this simplifies to 2 * n! / (d+1)
  (the editorial establishes a recurrence formula instead
   of that closed formula)
  We can directly get the simplified formula the following way:
  consider the function Fu, resp. Fv, that transforms any permutation
  into a "valid" one by swapping the first of the d+1 vertices of the path
  with u, resp. v. Each permutation in the image has exactly d+1 pre-images
  so that the image has n! / (d+1) elements. The "valid" permutations are
  the disjoint union for the images of both functions, so that their
  number is 2 * n! / (d+1)
*/

typedef long long ent;
typedef pair<int,int> couple;

const int P = 1000000009;
vector< vector<couple> > T;
vector<ent> dist,distw;

void dfs(int u) {
  for (vector<couple>::iterator it=T[u].begin(); it!=T[u].end(); ++it)
    if (dist[it->first]<0) {
      dist[it->first] = dist[u] + 1;
      distw[it->first] = (distw[u] + it->second)%P;
      dfs(it->first);
    }
}

ent bezout(ent a, ent b, ent &u, ent &v) {
  if (b==0) {
    u = 1;
    v = 0;
    return a;
  }
  ent u1,v1;
  ent g = bezout(b,a%b,u1,v1);
  u = v1;
  v = u1-(a/b)*v1;
  return g;
}

ent inv_mod(ent a, ent n=P) {
  ent u,v;
  bezout(a,n,u,v);
  return (u+n)%n;
}

int main() {
  int n;
  cin >> n;
  ent F = 1;
  for (ent i=2; i<=n; ++i) F = (F*i)%P;
  T.resize(n);
  dist.resize(n);
  distw.resize(n);
  for (int i=0; i<n-1; ++i) {
    int u,v,w;
    cin >> u >> v >> w; --u; --v;
    T[u].push_back(couple(v,w));
    T[v].push_back(couple(u,w));
  }
  ent E = 0;
  for (int u=0; u<n; ++u) {
    fill(dist.begin(),dist.end(),-1);
    fill(distw.begin(),distw.end(),-1);
    dist[u] = distw[u] = 0;
    dfs(u);
    for (int v=u+1; v<n; ++v)
      E = (E + F*((ent)distw[v]*(2*inv_mod(dist[v]+1))%P)%P)%P;
  }
  cout << (E+P)%P << endl;
  return 0;
}
