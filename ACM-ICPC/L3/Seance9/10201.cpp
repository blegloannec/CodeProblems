#include <iostream>
#include <vector>
using namespace std;

typedef long long ent;

const int CAP = 200;
const int CAP0 = CAP/2;
const ent INF = 1000000000;

int W;
vector<ent> D,P;
vector< vector<ent> > mem;

// Cout minimal pour partir de la k-ieme station
// avec la quantite E
ent cost(int k, int E) {
  if (mem[k][E]>=0) return mem[k][E];
  if (k==0) return E==CAP0 ? 0 : INF;
  ent res = INF;
  int d = D[k]-D[k-1];
  for (int e=0; e<=E && e+d<=CAP; ++e)
    res = min(res, cost(k-1,e+d) + (E-e)*P[k]);
  mem[k][E] = res;
  return res;
}

int main() {
  int cas,d,p;
  char buff[100];
  cin >> cas;

  while (cas-->0) {
    cin >> W;
    D.push_back(0);
    P.push_back(-1);
    cin.getline(buff,sizeof(buff));
    cin.getline(buff,sizeof(buff));
    while (sscanf(buff,"%d %d",&d,&p)==2) {
      if (d<=W) {
	D.push_back(d);
	P.push_back(p);
      }
      cin.getline(buff,sizeof(buff));
    }
    int K = D.size();
    mem.resize(K);
    for (int i=0; i<K; ++i) mem[i].resize(CAP+1,-1);
    ent res = INF;
    int d = W-D[K-1];
    for (int e=CAP0; e+d<=CAP; ++e)
      res = min(res, cost(K-1,e+d));
    if (res>=INF) cout << "Impossible" << endl;
    else cout << res << endl;
    if (cas>0) cout << endl;

    // cleaning
    D.clear();
    P.clear();
    mem.clear();
  }

  return 0;
}
