#include <iostream>
#include <vector>
#include <array>
#include <cassert>
using namespace std;

typedef array<int,4> tile;
#define DN 0
#define DS 1
#define DE 2
#define DW 3

int W,H,nb_nodes;
vector<string> G;
vector<tile> TilesNW[9][3][3], Sol;
vector< pair<int,int> > Nodes;
vector<int> Mult, Neigh[4];

void gen_tiles() {
  for (int n=0; n<=2; ++n)
    for (int s=0; s<=2; ++s)
      for (int e=0; e<=2; ++e)
	for (int w=0; w<=2; ++w)
	  TilesNW[n+s+e+w][n][w].push_back({n,s,e,w});
}

bool connected() {
  vector<int> Q {1};
  vector<bool> seen(nb_nodes+1,false);
  seen[0] = seen[1] = true;
  int cpt = 1;
  while (!Q.empty()) {
    int u = Q.back();
    Q.pop_back();
    for (int d=0; d<4; ++d)
      if (Sol[u][d]>0 && !seen[Neigh[d][u]]) {
	seen[Neigh[d][u]] = true;
	Q.push_back(Neigh[d][u]);
	++cpt;
      }
  }
  return cpt==nb_nodes;
}

bool non_crossing() {
  vector< vector<bool> > Spc(H,vector<bool>(W,false));
  for (int i=1; i<=nb_nodes; ++i) {
    if (Sol[i][DE]>0)
      for (int y=Nodes[i].second+1; y<Nodes[Neigh[DE][i]].second; ++y) {
	if (Spc[Nodes[i].first][y]) return false;
	Spc[Nodes[i].first][y] = true;
      }
    if (Sol[i][DS]>0)
      for (int x=Nodes[i].first+1; x<Nodes[Neigh[DS][i]].first; ++x) {
	if (Spc[x][Nodes[i].second]) return false;
	Spc[x][Nodes[i].second] = true;
      }
  }
  return true;
}

bool backtrack(int i=1) {
  if (i>nb_nodes) return connected() && non_crossing();
  int cn = get<DS>(Sol[Neigh[DN][i]]), cw = get<DE>(Sol[Neigh[DW][i]]);
  for (auto it=TilesNW[Mult[i]][cn][cw].begin(); it!=TilesNW[Mult[i]][cn][cw].end(); ++it) {
    if (get<DE>(*it)<=Mult[Neigh[DE][i]] && get<DS>(*it)<=Mult[Neigh[DS][i]]) {
      Sol.push_back(*it);
      if (backtrack(i+1)) return true;
      Sol.pop_back();
    }
  }
  return false;
}

int main() {
  gen_tiles();
  cin >> W;
  cin >> H;
  G.resize(H);
  for (int i=0; i<H; ++i) cin >> G[i];
  Nodes.push_back(make_pair(-1,-1));
  Mult.push_back(0);
  for (int d=0; d<4; ++d) Neigh[d].push_back(-1);
  vector<int> vpred(W,0);
  for (int i=0; i<H;  ++i) {
    int hpred = 0;
    for (int j=0; j<W; ++j)
      if (G[i][j]!='.') {
	int n = Nodes.size();
	Nodes.push_back(make_pair(i,j));
	Mult.push_back((int)G[i][j]-(int)'0');
	for (int d=0; d<4; ++d) Neigh[d].push_back(0);
	if (hpred!=0) {
	  Neigh[DW][n] = hpred;
	  Neigh[DE][hpred] = n;
	}
	if (vpred[j]!=0) {
	  Neigh[DN][n] = vpred[j];
	  Neigh[DS][vpred[j]] = n;
	}
	hpred = vpred[j] = n;
      }
  }
  nb_nodes = (int)Nodes.size()-1;
  Sol.push_back({0,0,0,0});
  assert(backtrack());
  for (int i=1; i<=nb_nodes; ++i) {
    if (Sol[i][DE]>0) cout << Nodes[i].second << ' ' << Nodes[i].first << ' ' << Nodes[Neigh[DE][i]].second << ' ' << Nodes[Neigh[DE][i]].first << ' ' << Sol[i][DE] << endl;
    if (Sol[i][DS]>0) cout << Nodes[i].second << ' ' << Nodes[i].first << ' ' << Nodes[Neigh[DS][i]].second << ' ' << Nodes[Neigh[DS][i]].first << ' ' << Sol[i][DS] << endl;
  }
  return 0;
}
