#include <iostream>
#include <vector>
#include <set>
#include <cassert>
using namespace std;

/*
  A priori il n'y pas d'algo "efficace" pour ce pb.
  D(X+d) = D(X) donc on peut supposer que 0 est le plus petit element de X.
  Des lors, max(X) = max(DX) et l'on connait les deux bornes de X.
  Supposons que l'on ait construit un debut de solution potentielle et que
  l'on ait retire du multiset toutes les distances entre les points deja utilises,
  alors la plus grande distance restante est necessairement la distance entre
  une borne de X et un nouveau point (car si c'etait la distance entre 2 points interieurs,
  dont au moins un est encore inconnu, alors il resterait une ditance strictement plus
  grande dans le multiset). Il y a deux possibilites pour ce point selon la borne choisie,
  on essayera les deux suivant un algo de backtracking.
*/
  
int MaX = 0;
set<int> X;

bool backtrack(multiset<int> &D) {
  if (D.empty()) return true;
  int nx = *D.rbegin(); // max(D)
  vector<int> Nx(1,nx);
  if (MaX-nx!=nx) Nx.push_back(MaX-nx);
  for (unsigned int i=0; i<Nx.size(); ++i) {
    if (X.find(Nx[i])!=X.end()) continue; // X est un ensemble, doublons non autorises
    multiset<int> ND = D; // copie
    bool valid = true;
    for (set<int>::iterator ix=X.begin(); ix!=X.end(); ++ix) {
      multiset<int>::iterator e = ND.find(abs(Nx[i]-*ix));
      if (e==ND.end()) {
	valid = false;
	break;
      }
      else ND.erase(e);
    }
    if (valid) {
      X.insert(Nx[i]);
      if (backtrack(ND)) return true;
      X.erase(Nx[i]);
    }
  }
  return false;
}

int main() {
  int a;
  multiset<int> D;
  while (cin >> a) {
    MaX = max(MaX,a);
    D.insert(a);
  }
  D.erase(D.find(MaX));
  X.insert(0);
  X.insert(MaX);
  assert(backtrack(D));
  for (set<int>::iterator ix=X.begin(); ix!=X.end(); ++ix)
    cout << *ix << ' ';
  cout << endl;
  return 0;
}
