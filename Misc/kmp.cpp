#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef vector<int> vint;

vector<int> prefs(string B) {
  vint P = vint(B.size(),0);
  P[0] = -1;
  int k = -1;
  for (int i=1; i<(int)B.size(); ++i) {
    while (k>=0 && B[i-1]!=B[k]) k = P[k];
    ++k;
    P[i] = k;
  }
  return P;
}

vint kmp(string A, string B) {
  vint pos;
  vint P = prefs(B);
  int k = 0;
  for (int i=0; i<(int)A.size(); ++i) {
    while (k>=0 && A[i]!=B[k]) k = P[k];
    ++k;
    if (k==(int)B.size()) {
      pos.push_back(i-(int)B.size()+1);
      // reset pour tous les matchs
      i = i-(int)B.size()+1;
      k = 0;
    }
  }
  return pos;
}

int main() {
  int C;
  cin >> C;
  for (int c=0; c<C; ++c) {
    string A,B;
    cin >> A >> B;
    vint res = kmp(A,B);
    if (res.size()==0)
      cout << "No Match!" << endl;
    else {
      for (vint::iterator it=res.begin(); it!=res.end(); ++it)
	cout << *it << ' ';
      cout << endl;
    }
  }
  return 0;
}
