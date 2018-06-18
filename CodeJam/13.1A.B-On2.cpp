#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> paire;
typedef long long ent;

#define NMAX 10001

int E,R,N;
vector<paire> V;
int Ein[NMAX], Eout[NMAX];

bool comp(paire p1, paire p2) {return (p1.second>p2.second);}

/* On peut toujours dépenser le max d'énergie sur la tâche de plus grande valeur.
   Imposer les quantités d'énergie E_in(i) et E_out(i) pour la tâche T(i) fixe des bornes inf :
   E_in(i)-R en sortie de T(i-1), E_in(i)-2R en sortie de T(i-2), etc.
   Et des bornes sup :
   E_out(i)+R en entrée de T(i+1), E_out+2R en entrée de T(i+1)
   On traite les tâches dans l'ordre décroissant de valeur. Pour chaque tâche :
    - On prend la conso max possible pour la tâche courante en tenant compte des bornes.
    - On met à jour les bornes des autres.
   O(NMAX^2)
*/

int main() {
  int T,v,curr;
  ent gain;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    V.clear();
    cin >> E >> R >> N;
    R = min(E,R);
    for (int i=0; i<N; ++i) {
      cin >> v;
      V.push_back(paire(i,v));
      Ein[i] = E;
      Eout[i] = 0;
    }
    sort(V.begin(),V.end(),comp);
    gain = 0;
    for (int i=0; i<(int)V.size(); ++i) {
      curr = V[i].first;
      gain += (ent)(Ein[curr]-Eout[curr])*(ent)V[i].second;
      for (int j=curr+1; j<N; ++j) Ein[j] = (int)min((ent)Ein[j],(ent)Eout[curr]+(ent)(j-curr)*(ent)R); // au secours ;-D
      for (int j=curr-1; j>=0; --j) Eout[j] = (int)max((ent)Eout[j],(ent)Ein[curr]-(ent)(curr-j)*(ent)R);
    }
    cout << "Case #" << t << ": " << gain << endl;
  }
  return 0;
}
