#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int S;
    string P,Q;
    cin >> S >> P >> Q;
    int L = P.size(), M = 0;
    for (int d=-L+1; d<L; ++d) {
      // on aligne P[i] avec Q[i+d]
      vector<int> H(1,0);
      for (int i=max(0,-d); i<min(L,L-d); ++i)
	H.push_back(H[(int)H.size()-1]+(P[i]!=Q[i+d]?1:0));
      int r = 1;
      for (int l=0; l<(int)H.size(); ++l) {
	while (r+1<(int)H.size() && H[r+1]-H[l]<=S) ++r;
	M = max(M,r-l);
      }
    }
    cout << M << endl;
  }
  return 0;
}
