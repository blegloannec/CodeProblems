#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

// Kinda bucket sorting using Fenwick Trees

/* Fenwick Trees */
const int L = 10000001;
vector<int> A(L);

void add(int i, int v=1) {
  assert(i>0);
  while (i<L) {
    A[i] += v;
    i += i&-i;
  }
}

int sum_prefix(int i) {
  int s = 0;
  while (i>0) {
    s += A[i];
    i -= i&-i;
  }
  return s;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N;
    cin >> N;
    fill(A.begin(),A.end(),0);
    long long res = 0;
    for (int n=0; n<N; ++n) {
      int a;
      cin >> a;
      add(a);
      res += n-sum_prefix(a)+1;
    }
    cout << res << endl;
  }
  return 0;
}
