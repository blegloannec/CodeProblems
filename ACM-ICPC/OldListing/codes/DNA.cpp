// DNA sorting

#include <iostream>
#include <string>
#include <list>
using namespace std;

/* Un majorant du nb d'inversions est 
   n(n-1)/2 pour un mot de taille n.
*/

#define MAX 1300

int n;
list<string> t[MAX];

int nb_inv(string &s) {
  int a,c,g,res;
  a = c = g = res = 0;
  string::reverse_iterator it;
  for (it=s.rbegin(); it!=s.rend(); it++) {
    if (*it=='A') ++a;
    else if (*it=='C') {
      ++c;
      res += a;
    }
    else if (*it=='G') {
      ++g;
      res += a+c;
    }
    else res += a+c+g;
  }
  return res;
}

int main() {
  string s;
  int M,m;
  cin >> M;
  
  while (M-->0) {
    for (int i=0; i<MAX; i++) t[i].clear();
    cin >> n >> m;
    for (int i=0; i<m; i++) { // tri lineaire
      cin >> s;
      t[nb_inv(s)].push_back(s);
    }
    for (int i=0; i<MAX; i++) {
      while (!t[i].empty()) {
	cout << t[i].front() << '\n';
	t[i].pop_front();
      }
    }
    if (M>0) cout << '\n';
  }

  return 0;
}
