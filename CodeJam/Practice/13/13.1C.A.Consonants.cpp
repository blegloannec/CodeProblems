#include <iostream>
using namespace std;

#define ISVOY(C) ((C)=='a' || (C)=='e' || (C)=='i' || (C)=='o' || (C)=='u')
typedef unsigned long long ent;

int main() {
  int T,n;
  string mot;
  ent cpt; // compte les sous-mots
  int currbloc; // nb courant de consonnes consecutives
  int lastbloc; // position du dernier bloc de n consonnes consecutives
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cin >> mot >> n;
    cpt = 0;
    currbloc = 0;
    lastbloc = -1;
    for (int p=0; p<(int)mot.size(); ++p) {
      if (ISVOY(mot[p])) currbloc = 0;
      else currbloc += 1;
      if (currbloc >= n) lastbloc = p-n+1;
      if (lastbloc >= 0) cpt += (ent)(lastbloc+1);
    }
    cout << "Case #" << t << ": " << cpt << endl;
  }
  return 0;
}
