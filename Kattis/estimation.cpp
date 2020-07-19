#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int INF = 1<<30;

int N, K;
vector<int> A;

// DP in O(N^2 * (K + log N))
int dp() {
  vector< vector<int> > DP(N+1, vector<int>(K+1, INF));
  DP[0][0] = 0;
  for (int i=1; i<=N; ++i) {
    priority_queue<int> Top, Bot;
    int TopSum = 0, BotSum = 0;
    for (int j=i; j>0; --j) {
      // here we consider A[j..i] as last block
      // we pick its median as representative to minimize the cost
      // running median (using 2 heaps) update
      if (Bot.empty() || A[j]<=Bot.top()) {
	Bot.push(A[j]);
	BotSum += A[j];
      }
      else {
	Top.push(-A[j]);
	TopSum += A[j];
      }
      if (Top.size() > Bot.size()) {
	int x = -Top.top(); Top.pop();
	TopSum -= x;
	Bot.push(x);
	BotSum += x;
      }
      else if (Top.size()+1 < Bot.size()) {
	int x = Bot.top(); Bot.pop();
	BotSum -= x;
	Top.push(-x);
	TopSum += x;
      }
      // DP[i] update considering A[j..i] as last block
      int med = Bot.top();
      int cost = TopSum-Top.size()*med + Bot.size()*med-BotSum;
      for (int k=1; k<=K; ++k)
	if (DP[j-1][k-1]<INF)
	  DP[i][k] = min(DP[i][k], DP[j-1][k-1] + cost);
    }
  }
  return DP[N][K];
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> N >> K;
  A.resize(N+1);
  for (int i=1; i<=N; ++i) cin >> A[i];
  cout << dp() << endl;
  return 0;
}
