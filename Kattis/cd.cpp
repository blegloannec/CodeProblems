#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
  int N,M;
  while (true) {
    cin >> N >> M;
    if (N==0 && M==0) break;
    unordered_set<int> A;
    for (int i=0; i<N; ++i) {
      int a;
      cin >> a;
      A.insert(a);
    }
    int res = 0;
    for (int i=0; i<M; ++i) {
      int b;
      cin >> b;
      if (A.find(b)!=A.end()) ++res;
    }
    cout << res << endl;
  }
  return 0;
}
