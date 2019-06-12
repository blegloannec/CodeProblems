#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>
using namespace std;

int N;
vector<int> S;

int greedy_teams() {
  sort(S.begin(), S.end());
  unordered_map< int, priority_queue<int> > Q;
  for (int i : S) {
    // we add i to the smallest team ending with i-1 (if such a team exists)
    int s = 1;
    if (!Q[i-1].empty()) {
      s = -Q[i-1].top() + 1;
      Q[i-1].pop();
    }
    Q[i].push(-s);
  }
  int res = N;
  for (auto it : Q)
    if (!it.second.empty())
      res = min(res, -it.second.top());
  return res;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; ++t) {
    scanf("%d", &N);
    S.resize(N);
    for (int i=0; i<N; ++i) scanf("%d", &S[i]);
    printf("%d\n", greedy_teams());
  }
  return 0;
}
