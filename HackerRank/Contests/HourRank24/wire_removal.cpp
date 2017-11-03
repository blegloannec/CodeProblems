#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

ll n, E=0, D=0;
vector< vector<int> > G;

int dfs(int u=0, int u0=-1, ll d=0) {
  ll f = 1;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) f += dfs(*iv,u,d+1);
  E += d*(n-f);
  D += d;
  return f;
}

int main() {
  scanf("%lld",&n);
  G.resize(n);
  for (int i=0; i<n-1; ++i) {
    int x,y;
    scanf("%d %d",&x,&y); --x; --y;
    G[x].push_back(y);
    G[y].push_back(x);
  }
  dfs();
  printf("%f\n",(double)E/D);
  return 0;
}
