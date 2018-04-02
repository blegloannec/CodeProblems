#include <iostream>
#include <vector>
#include <string>
using namespace std;

void prefs(string &B, vector<int> &P) {
  P.resize(B.size()+1);
  P[0] = -1;
  int k = -1;
  for (int i=1; i<=(int)B.size(); ++i) {
    while (k>=0 && B[i-1]!=B[k]) k = P[k];
    ++k;
    P[i] = k;
  }
}

vector<int> kmp(string &A, string &B) {
  vector<int> pos;
  vector<int> P;
  prefs(B,P);
  int k = 0;
  for (int i=0; i<(int)A.size(); ++i) {
    while (k>=0 && A[i]!=B[k]) k = P[k];
    ++k;
    if (k==(int)B.size()) {
      pos.push_back(i-(int)B.size()+1);
      k = P[k];
    }
  }
  return pos;
}

int main() {
  string A,B;
  while (getline(cin,A)) {
    getline(cin,B);
    vector<int> res = kmp(B,A);
    for (vector<int>::iterator it=res.begin(); it!=res.end(); ++it) {
      if (it!=res.begin()) cout << ' ';
      cout << *it;
    }
    cout << endl;
  }
  return 0;
}
