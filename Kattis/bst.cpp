// O(n log n)
#include <iostream>
#include <vector>
#include <set>
using namespace std;

set<int> S;    // bornes inf des intervalles de valeurs non encore inserees
vector<int> D; // profondeurs associees

int main() {
  int n;
  cin >> n;
  D.resize(n+2,0);
  long long res = 0;
  S.insert(1);
  for (int i=0; i<n; ++i) {
    int x;
    cin >> x;
    auto it = S.upper_bound(x); --it;
    int x0 = *it;
    /* x appartient a l'intervalle [x0,?] et sera insere a la
       profondeur D[x0]. Apres son insertion, les intervalles
       [x0,x-1] et [x+1,?] seront a la profondeur D[x0]+1. */
    res += D[x0];
    ++D[x0];
    S.insert(x+1);
    D[x+1] = D[x0];
    cout << res << endl;
  }
  return 0;
}
