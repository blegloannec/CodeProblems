#include <iostream>
#include <vector>
#include <set>
using namespace std;

/*
  Soit D(i,j) = max(i,j) - min(i,j), pour i <= j.
  Si a1 <= a2 <= b2 <= b1 alors D(a2,b2) <= D(a1,b1).
  Il est suffisant de savoir calculer le nb de paires
  pour lesquelles D(a,b) <= H pour H quelconque.
  
  Pour a fixe, D(a,b) est croissant selon b, ainsi
  on pourrait chercher, pour chaque a, le b limite
  par recherche dicho (sachant qu'avec une structure
  adaptee on peut avoir le min/max d'une plage en O(log n))
  et donc resoudre chaque requete en O(n log^2 n).
  
  Mais on peut faire mieux et plus simple, car si
  l'on connait le b limite pour a fixe, alors
  pour a-1, le b limite est plus petit et l'on peut
  decroitre b jusqu'a le trouver, en utilisant un BST
  (ici multiset en C++) pour stocker les valeurs de
  l'intervalle [a,b] et avoir le D(a,b) en O(log n).
  Ainsi on resout chaque requete en O(n log n).
*/

int n,q;
vector<int> A;

int D(multiset<int> &S) {
  multiset<int>::iterator end = S.end();
  return *(--end) - *(S.begin());
}

long long count(int x) {
  long long cpt = 0LL;
  multiset<int> S;
  int b = n-1;
  for (int a=n-1; a>=0; --a) {
    S.insert(A[a]);
    // Attention: erase(val) sur un multiset
    // retire TOUTES les valeurs = val !
    // Donc erase(iterator) obligatoire ici.
    while (a<=b && D(S)>x) S.erase(S.find(A[b--]));
    cpt += b-a+1;
  }
  return cpt;
}

int main() {
  cin >> n >> q;
  A.resize(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  for (int t=0; t<q; ++t) {
    int l,h;
    cin >> l >> h;
    cout << count(h)-count(l-1) << endl;
  }
  return 0;
}
