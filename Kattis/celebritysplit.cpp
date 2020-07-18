#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, S, best;
vector<int> X, R;

void backtrack(int i, int a=0, int b=0) {
  if (a==b) best = min(best, S-a-b);
  if (i>=0 && S-(a+b+R[i])<best && abs(a-b)<=R[i]) {
    backtrack(i-1, a+X[i], b);
    backtrack(i-1, a, b+X[i]);
    backtrack(i-1, a, b);
  }
}

int main() {
  while (true) {
    cin >> N;
    if (N==0) break;
    X.resize(N);
    S = 0;
    for (int i=0; i<N; ++i) {
      cin >> X[i];
      S += X[i];
    }
    sort(X.begin(), X.end());
    R = X;
    for (int i=1; i<N; ++i)
      R[i] += R[i-1];
    best = S;
    backtrack(N-1);
    cout << best << endl;
  }
  return 0;
}
