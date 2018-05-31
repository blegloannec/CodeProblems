/*
  On a une prog. dyn. evidente en R*B*P pour P = nb de point
  c'est clairement O((R*B)^2) ici mais on peut mieux faire.

  On remarque qu'une solution pour (R,B) peut toujours se "compacter"
  en une solution de meme taille pour (R',B') avec R'<=R et B'<=B en
  remplacant tout point (r,b) par (r-1,b) ou (r,b-1), s'ils ne sont pas tous
  deux deja pris, et en iterant ce processus autant que possible sur tous les
  points.
  Une solution "compacte" ainsi obtenue est alors une union de "rectangles"
  ancres en (0,0) (et en excluant ce point).
  On peut se ramener a ne chercher que les solutions "compactes".
  Si une solution compacte pour (R,B) contient le point (r,b), alors elle
  contient tous les (r',b') avec r'<=r et b'<=b (sauf (0,0) qui ne compte pas).
  Des lors R >= (1+2+...+r)*(b+1) = r*(r+1)/2 * (b+1)
        et B >= (1+2+...+b)*(r+1) = b*(b+1)/2 * (r+1)
  et l'on se ramene a un nb de points P = O((R*B)^(1/3)).
*/
#include <iostream>
#include <vector>
using namespace std;

const int M = 500;
vector< vector<int> > D(M+1);
vector<int> PR,PB;

void dp() {
  for (int i=0; i<=M; ++i) D[i].resize(M+1,0);
  for (int i=0; i<=M; ++i)
    for (int j=0; j<=M; ++j)
      if (!(i==0 && j==0) && M>=(j+1)*i*(i+1)/2 && M>=(i+1)*j*(j+1)/2) {
	PR.push_back(i);
	PB.push_back(j);
      }
  for (unsigned int p=0; p<PR.size(); ++p) {
    for (int R=M; R>=PR[p]; --R)
      for (int B=M; B>=PB[p]; --B)
	D[R][B] = max(D[R][B], 1+D[R-PR[p]][B-PB[p]]);
  }
}

int main() {
  dp();
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    int R,B;
    cin >> R >> B;
    cout << "Case #" << t << ": " << D[R][B] << endl;
  }
  return 0;
}
