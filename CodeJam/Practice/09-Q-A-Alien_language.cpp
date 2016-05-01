// Nb : plus facile en python en interprétant directement le pattern comme une regexp python (remplacer (...) par [...])

#include <iostream>
using namespace std;

int L,D,N;
int mots[5000][15];
bool pattern[15][26];

bool match(int n) {
  // vérifie si mots[n] match le pattern
  for (int i=0; i<L; ++i)
    if (!pattern[i][mots[n][i]]) return false;
  return true;
}

int main() {
  char r;
  int cpt;
  cin >> L >> D >> N;
  // on stocke les mots
  for (int i=0; i<D; ++i)
    for (int j=0; j<L; ++j) {
      cin >> r;
      mots[i][j] = (int)r-(int)'a';
    }
  for (int n=1; n<=N; ++n) {
    // on efface le pattern
    for (int i=0; i<15; ++i)
      for (int j=0; j<26; ++j)
	pattern[i][j] = false;
    // on parse le pattern
    for (int c=0; c<L; ++c) {
      cin >> r;
      if (r=='(') {
	cin >> r;
	while (r!=')') {
	  pattern[c][(int)r-(int)'a'] = true;
	  cin >> r;
	}
      }
      else pattern[c][(int)r-(int)'a'] = true;
    }
    // on compte le nb de mots qui matchent
    cpt = 0;
    for (int i=0; i<D; ++i)
      if (match(i)) ++cpt;
    cout << "Case #" << n << ": " << cpt << endl;
  }
  return 0;
}
