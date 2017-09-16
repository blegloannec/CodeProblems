#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int> &B1, vector<int> &B2, vector<int> &B) {
  unsigned int i1 = 0, i2 = 0;
  while (i1<B1.size() || i2<B2.size()) {
    if (i1<B1.size() && (i2==B2.size() || B1[i1]<=B2[i2]))
      B.push_back(B1[i1++]);
    else B.push_back(B2[i2++]);
  }
}

int main() {
  int n;
  cin >> n;
  vector<int> A(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  cin >> n;
  vector<int> B(n),C;
  for (int i=0; i<n; ++i) cin >> B[i];
  merge(A,B,C);
  for (unsigned int i=0; i<C.size(); ++i) {
    cout << C[i];
    if (i==C.size()-1) cout << endl;
    else cout << ' ';
  }
  return 0;
}
