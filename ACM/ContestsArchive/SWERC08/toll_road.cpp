#include <iostream>
#include <vector>
#include <map>
using namespace std;

typedef pair<int,int> paire;
typedef vector<paire> liste;

#define MAX 200001
liste g[MAX];
bool visited[MAX];

/* Le sous-arbre de poids maximal
   Généralisation diviser pour régner de la plus grande somme
   consécutive 
   Retourne la plus grande somme enracinée dans res_rooted
   et la plus grande somme intérieure en res_inside
*/
   
int max_subtree(int root, int& res_rooted) {
  visited[root] = true;
  int rr,ri;
  res_rooted = 0;
  int res_inside = 0;
  for (int i=0; i<(int)g[root].size(); ++i)
    if (!visited[g[root][i].first]) {
      ri = max_subtree(g[root][i].first,rr);
      res_rooted = max(rr+g[root][i].second+res_rooted,res_rooted);
      res_inside = max(res_rooted,max(res_inside,ri));
    }
  return res_inside;
}

int main() {
  int n,a,b,p;
  while (cin >> n) {
    if (n==0) return 0;
    for (int i=0; i<MAX; ++i) {
      g[i].clear();
      visited[i] = false;
    }
    for (int i=0; i<n; ++i) {
      cin >> a >> b >> p;
      g[a].push_back(paire(b,p));
      g[b].push_back(paire(a,p));
    }
    cout << max_subtree(a,p) << endl;
  }
  return 0;
}
