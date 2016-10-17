#include <iostream>
#include <queue>
using namespace std;

/* Un code a N elements peut etre represente par un arbre binaire a N
   feuilles. Descendre a gauche pour un 0 et a droite pour un 1. 
   Le poids d'une feuille est le poids de son chemin depuis la racine
   (cout 1 pour les 0 et 4 pour les 1).
   Un arbre de code optimal est "sature" : tout noeud interne a 2 fils.
   Algo glouton : pour construire un code optimal d'ordre N+1 a partir d'un
   code optimal d'ordre N, prendre la feuille de plus petit poids x et creer
   2 fils a cet endroit (de poids x+1 et x+4).

   Runs in <2min avec -O3.
*/

const int N = 1000000000;

int main() {
  priority_queue<int> q;
  long long s = 0;
  q.push(0);
  for (int i=1; i<N; ++i) {
    int x = -q.top();
    q.pop();
    q.push(-(x+1));
    q.push(-(x+4));
    s += x+5;
  }
  cout << s << endl;
  return 0;
}
