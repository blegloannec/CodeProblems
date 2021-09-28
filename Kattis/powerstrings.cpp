#include <iostream>
#include <vector>
#include <string>
using namespace std;

void prefs(const string &B, vector<int> &P) {
  P.resize(B.size()+1);
  P[0] = -1;
  int k = -1;
  for (int i=1; i<=(int)B.size(); ++i) {
    while (k>=0 && B[i-1]!=B[k]) k = P[k];
    ++k;
    P[i] = k;
  }
}

int kmp(const string &A, const string &B, int i0=0) {
  vector<int> P;
  prefs(B,P);
  int k = 0;
  for (int i=i0; i<(int)A.size(); ++i) {
    while (k>=0 && A[i]!=B[k]) k = P[k];
    ++k;
    if (k==(int)B.size())
      return i-(int)B.size()+1;
  }
  return -1;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  while (true) {
    string S;
    cin >> S;
    if (S==".") break;
    int i = kmp(S+S, S, 1);
    cout << S.size()/i << endl;
  }
  return 0;
}
