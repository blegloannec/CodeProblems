#include <iostream>
#include <vector>
using namespace std;

/*
   Il s'agit de deplacer les serpents de facon a ce qu'ils s'intersectent 2 a 2.
   Si un ensemble d'intervalles s'intersectent 2 a 2, alors ils s'intersectent
   globalement : par exemple, a l'instant ou se termine l'intervalle se
   terminant en premier, car alors tous les intervalles doivent avoir demarre
   mais par definition aucun n'a termine.
   Le raisonnement symetrique sur les debuts d'intervalles montre que
   l'intersection des [Li,Ri] est l'intervalle [max_i(Li),min_i(Ri)].
   Chaque serpent represente un intervalle horizontal et un intervalle vertical.
   Chaque ensemble s'intersecte 2 a 2, donc globalement, donc il y a une abscisse
   commune et une ordonnee commune et donc un point 2D commun d'intersection.
   On notera que l'on cherche a minimiser le max sur les serpents des dx+dy,
   donc on ne peut pas traiter les deplacements en x et y independamment, mais
   comme l'espace est de taille 50 x 50 au plus, on peut betement essayer
   tous les points d'intersection et calculer la distance en O(n) pour chaque point.
   Comme n est au plus 50, chaque testcase est en O(50^3).
   Il y a au plus 5 testcases, donc globalement O(50^4).

   Cette approche passe en C++ mais pas en Python/Pypy.

   NB : Une approche dichotomique 2D est peut-etre envisageable pour trouver le
   point d'intersection en O(log(50)) ? A voir, les bonnes proprietes de "monotonie"
   necessaires ne sont pas claires ici...
*/

int dist(int l, int r, int x) {
  if (l<=x && x<=r) return 0;
  if (x<l) return l-x;
  return x-r;
}

int main() {
  int T,n,x1,y1,x2,y2;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> n;
    vector<int> X1(n),X2(n),Y1(n),Y2(n);
    for (int i=0; i<n; ++i) {
      cin >> x1 >> y1 >> x2 >> y2;
      X1[i] = min(x1,x2); X2[i] = max(x1,x2);
      Y1[i] = min(y1,y2); Y2[i] = max(y1,y2);
    }
    int dmin = 1<<30;
    for (int x=1; x<=50; ++x)
      for (int y=1; y<=50; ++y) {
	int d = 0;
	for (int i=0; i<n; ++i)
	  d = max(d,dist(X1[i],X2[i],x)+dist(Y1[i],Y2[i],y));
	dmin = min(dmin,d);
      }
    cout << dmin << endl;
  }
  return 0;
}
