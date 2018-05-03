#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

int n;
vector< vector< pair<int,double> > > G;
vector<double> Dist;
unordered_map<string,int> I;

bool bellman_ford(int u0=0) {
  Dist.resize(n,1e9);
  Dist[u0] = 0.;
  for (int k=0; k<n-1; ++k)
    for (int u=0; u<n; ++u)
      for (auto iv=G[u].begin(); iv<G[u].end(); ++iv)
	Dist[iv->first] = min(Dist[iv->first], Dist[u] + iv->second);
  // checking for negative cycles
  for (int u=0; u<n; ++u)
    for (auto iv=G[u].begin(); iv<G[u].end(); ++iv)
      if (Dist[u] + iv->second < Dist[iv->first]) return false;
  return true;
}

double weight(string &s) {
  int i = s.find(":");
  int p = stoi(s.substr(0,i)), q = stoi(s.substr(i+1,s.size()));
  double w = log((double)p/q);
  return w;
}

int main() {
  while (true) {
    cin >> n;
    if (n==0) break;
    for (int i=0; i<n; ++i) {
      string s;
      cin >> s;
      I[s] = i;
    }
    G.resize(n);
    int m;
    cin >> m;
    for (int i=0; i<m; ++i) {
      string su,sv,sw;
      cin >> su >> sv >> sw;
      int u = I[su];
      int v = I[sv];
      double w = weight(sw);
      G[u].push_back(make_pair(v,w));
    }
    if (bellman_ford()) cout << "Ok" << endl;
    else cout << "Arbitrage" << endl;
    // cleaning
    G.clear();
    Dist.clear();
    I.clear();
  }
  return 0;
}
