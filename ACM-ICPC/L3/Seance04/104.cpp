/* Arbitrage
   L'algo de prog dyn utilisé ici est en n^4
   En utilisant l'exponentiation rapide et des produits de matrice, on peut faire du n^3 * log(n)
   Mais le problème ne demande pas les chemins de poids minimaux mais le chemin de poids strictement négatif et de longueur minimal (du moins on s'y ramène), ce qui impose la version linéaire.
*/


#include <iostream>
#include <math.h>
#include <list>
using namespace std;

#define MAX 22

int n,k;
float t[MAX][MAX][MAX];
int pi[MAX][MAX][MAX];
list<int> vert;


/*// Version sans memorisation du chemin
void ProgDynPaires() {
  for (int k=2; k<=n; k++)
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++) {
	t[k][i][j] = t[k-1][i][j];
	for (int l=0; l<n; l++)
	  t[k][i][j] = min(t[k][i][j],t[k-1][i][l]+t[1][l][j]);
      }
}
*/


int ProgDynPaires() {
  float c;
  for (int i=0; i<n; i++)
    for (int j=0; j<n; j++) 
      pi[1][i][j] = i;
  for (k=2; k<=n; k++)
    for (int i=0; i<n; i++) 
      for (int j=0; j<n; j++) {
	t[k][i][j] = t[k-1][i][j];
	for (int l=0; l<n; l++) {
	  c = t[k-1][i][l] + t[1][l][j];
	  if (t[k][i][j] > c) {
	    t[k][i][j] = c;
	    pi[k][i][j] = l;
	  }
	}
	if ((i==j)&&(t[k][i][i]<=-log(1.01))) return i;
      }
  return -1;
}


void Chemin(int r) {
  vert.clear();
  vert.push_front(r+1);
  int cc = pi[k][r][r];
  while (k>=1) {
    vert.push_front(cc+1);
    cc = pi[--k][r][cc];
  }
}  
  

int main() {
  float f;
  int res;
  list<int>::iterator it;

  while (cin >> n) {
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++) {
	if (i==j) t[1][i][j] = 0;
	else { 
	  cin >> f;
	  t[1][i][j] = -log(f);
	}
      }
    
    res = ProgDynPaires();
    
    if (res<0) cout << "no arbitrage sequence exists\n";
    else {
      Chemin(res);
      cout << *(vert.begin());
      for (it=++vert.begin(); it!=vert.end(); it++) 
	cout << ' ' << *it;
      cout << '\n';
    }
  }

  return 0;
}
