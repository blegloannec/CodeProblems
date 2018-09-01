#include <iostream>
#include <map>
using namespace std;

/*
  L'issue ne depend que des positions des facteurs P dans S.
  On peut faire une prog. dyn. quadratique, mais ce n'est pas suffisant.
  
  Il faut pousser l'analyse du jeu en question pour arriver a une solution
  satisfaisante.
  On remarque que si S = XPY avec |X| = |Y|, alors Amanda gagne toujours
  en jouant a chaque tour du cote oppose au dernier choix de Steven.
  De facon symetrique, si Steven peut forcer Amanda a jouer sur une position
  dans laquelle P n'est pas au milieu, alors il gagne.

  Notons R = |S|-|P|
  1. La remarque precedente nous assure que si R est pair et que
  P est au milieu de S, i.e. en position R/2 alors Amanda gagne.
  2. Si R est pair et que P est a la fois est en position (R-2)/2 et (R+2)/2,
  i.e. au milieu de S prive de ses 2 premiers caracteres mais aussi au
  milieu de S prive de ses 2 derniers caracteres, alors Amanda gagne en
  jouant au premier coup du meme cote que Steven, ce qui ramene a une position
  du cas 1.
  3. Si R impair et que P n'est pas en position (R-1)/2 ou n'est pas en (R+1)/2,
  alors Steven gagne en forcant Amanda a jouer sur une position paire sans P au
  milieu.
  4. Complementaire de 3
  Si R impair et que P est a la fois est en position (R-1)/2 et (R+1)/2,
  alors comme P est aux 2 positions centrales, Amanda gagne en jouant toujours
  du cote oppose a Steven, ce qui force a rester dans le cas 4, jusqu'a R=1
  ou Steven fera apparaitre P quel que soit son choix.
  5. Complementaire de 1 et 2
  Si R est pair, n'est pas en position R/2 et [n'est pas en (R-2)/2 ou n'est pas
  en (R+2)/2], alors disons sans perte de generalite que P n'est pas en (R-2)/2,
  Steven joue en derniere position, forcant Amanda a jouer sur R impair avec
  P qui n'est present sur aucune des 2 positions centrales, il peut donc jouer
  a chaque fois du cote oppose a Amanda qui sera contrainte a la defaite quel
  que soit son dernier coup.
*/

string S,P;

// O(|P|)
bool win_form() {
  int R = S.size()-P.size();
  if (R<0) return true;
  if (R==0) return S!=P;
  if (R%2==0)
    return S.compare(R/2,P.size(),P) && (S.compare(R/2-1,P.size(),P) || S.compare(R/2+1,P.size(),P));
  return S.compare((R-1)/2,P.size(),P) || S.compare((R+1)/2,P.size(),P);
}

int main() {
  int q;
  cin >> q;
  for (int t=0; t<q; ++t) {
    cin >> S;
    cin >> P;
    cout << (win_form() ? "Steven" : "Amanda") << endl;
  }
  return 0;
}


// =====
// DP en O(n^2) qui passe quelques testcases (20/55 pts)
typedef pair<int,int> couple;
map<couple,bool> memo;
bool win(int a, int b, bool s=false) {
  couple k = make_pair(a,b);
  if (memo.find(k)!=memo.end()) return s^memo[k];
  if (b-a+1<=(int)P.size()) return s^true;
  bool res = !(win(a+1,b,!s) && win(a,b-1,!s));
  memo[k] = s^res;
  return res;
}

int main_dp() {
  int q;
  cin >> q;
  for (int t=0; t<q; ++t) {
    cin >> S;
    cin >> P;
    size_t i = S.find(P);
    while (i!=string::npos) {
      memo[make_pair(i,i+P.size()-1)] = false;
      // petit. optim. suite a la remarque de base :
      for (int j=1; 0<=i-j && i+P.size()-1+j<S.size(); ++j)
	memo[make_pair(i-j,i+P.size()-1+j)] = false;
      i = S.find(P,i+1);
    }
    if (memo.size()==0 || win(0,S.size()-1))
      cout << "Steven" << endl;
    else cout << "Amanda" << endl;
    memo.clear();
  }
  return 0;
}
