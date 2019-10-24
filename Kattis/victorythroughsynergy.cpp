// proper backtrack for a pb that could easily be brute-forced...
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int N = 10;
vector<int> G[N], Control[N+1], Order(N);
int PlayerAt[N], Score[N][N];
string Nation[N], League[N], Team[N];
vector<bool> Used(N,false);

bool backtrack(int i=0) {
  for (int u : Control[i]) {
    int s = 0;
    for (int v : G[u]) s += Score[PlayerAt[u]][PlayerAt[v]];
    if (s<(int)G[u].size()) return false;
  }
  if (i==N) return true;
  int u = Order[i];
  for (int p=0; p<N; ++p)
    if (!Used[p]) {
      PlayerAt[u] = p;
      Used[p] = true;
      if (backtrack(i+1)) return true;
      Used[p] = false;
    }
  return false;
}

void init() {
  for (int i=0; i<N; ++i)
    for (int j=i+1; j<N; ++j) {
      int s = 0;
      if (Nation[i]==Nation[j]) s = 1;
      if (Team[i]==Team[j]) s += 2;
      else if (League[i]==League[j]) ++s;
      Score[i][j] = Score[j][i] = s;
    }
  vector<int> Time(N);
  for (int i=0; i<N; ++i) Order[i] = i;
  sort(Order.begin(), Order.end(), [](int i, int j){return G[i].size()>G[j].size();});
  for (int t=0; t<N; ++t) Time[Order[t]] = t;
  for (int u=0; u<N; ++u) {
    int t = Time[u];
    for (int v : G[u]) t = max(t,Time[v]);
    Control[t+1].push_back(u);
  }
}

int main() {
  int M;
  cin >> M;
  for (int i=0; i<M; ++i) {
    int a,b;
    cin >> a >> b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  for (int i=0; i<N; ++i) {
    string name;
    cin >> name >> Nation[i] >> League[i] >> Team[i];
  }
  init();
  cout << (backtrack() ? "yes" : "no") << '\n';
  return 0;
}
