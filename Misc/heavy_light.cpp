#include <iostream>
#include <vector>
using namespace std;

/* 
   A nice reference:
   https://blog.anudeep2011.com/heavy-light-decomposition/
*/

int N;
vector< vector<int> > G;


/* --- HL --- */
vector<int> HLSucc,HLPathIndex,HLIndex,HLPred;
vector<bool> HLStart;
vector< vector<int> > HLPath;

int dfs_hl(int u=0, int u0=-1) {
  HLPred[u] = u0;
  int l = 1, lvmax = 0;
  for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      int lv = dfs_hl(*iv,u);
      l += lv;
      if (lv>lvmax) {
	lvmax = lv;
	HLSucc[u] = *iv;
      }
    }
  if (HLSucc[u]>=0)
    HLStart[HLSucc[u]] = false;
  return l;
}

void hl_init() {
  HLSucc.clear();         // cleaning (if needed)
  HLSucc.resize(N,-1);
  HLStart.clear();        // cleaning
  HLStart.resize(N,true);
  HLPred.resize(N);
  dfs_hl();
  HLPath.clear();         // cleaning
  HLPathIndex.resize(N);
  HLIndex.resize(N);
  for (int u=0; u<N; ++u)
    if (HLStart[u]) {
      int pi = HLPath.size();
      HLPath.resize(pi+1);
      int v = u;
      while (v>=0) {
	HLPathIndex[v] = pi;
	HLIndex[v] = HLPath[pi].size();
	HLPath[pi].push_back(v);
	v = HLSucc[v];
      }
    }
}
/* ------ */


int main() {
  cin >> N;
  G.resize(N);
  for (int i=0; i<N-1; ++i) {
    int u,v;
    cin >> u >> v; --u; --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  hl_init();
  for (unsigned int i=0; i<HLPath.size(); ++i) {
    for (unsigned int j=0; j<HLPath[i].size(); ++j) {
      int v = HLPath[i][j];
      cout << " -> " <<  v+1 << " (" << HLPathIndex[v] << ":" << HLIndex[v] << ")";
    }
    cout << endl;
  }
  return 0;
}
