#include <iostream>
#include <vector>
using namespace std;

const int M = 200000001;

int main() {
  int u,m;
  cin >> u >> m;
  vector<bool> used(M, false);
  used[u] = true;
  vector<int> U(1,u);
  int d = 1;
  while (!used[m]) {
    while (used[d]) ++d;
    u += d;
    used[u] = true;
    for (int v : U) used[u-v] = true;
    U.push_back(u);
  }
  cout << U.size() << endl;
  return 0;
}
