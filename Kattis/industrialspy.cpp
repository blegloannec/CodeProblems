#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool prime(int N) {
  if (N<=2 || (N&1)==0) return N==2;
  for (int d=3; d*d<=N; d+=2)
    if (N%d==0) return false;
  return true;
}

int subprimes(vector<int> &Digits) {
  sort(Digits.begin(), Digits.end());
  vector<int> Gen;
  do {
    int n = 0;
    for (int d : Digits) {
      n = 10*n + d;
      Gen.push_back(n);
    }
  }
  while (next_permutation(Digits.begin(), Digits.end()));
  sort(Gen.begin(), Gen.end());
  int res = (int)prime(Gen[0]);
  for (int i=1; i<(int)Gen.size(); ++i)
    if (Gen[i]!=Gen[i-1] && prime(Gen[i])) ++res;
  return res;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    string N;
    cin >> N;
    vector<int> D;
    for (char c : N) D.push_back(c-'0');
    cout << subprimes(D) << endl;
  }
  return 0;
}
