#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

// Moore-Hogdson scheduling algorithm
// pb 1153 in UVa, 3507 in Archive

struct job {
  int q,d;  // quantity, deadline
  job(int q, int d) : q(q), d(d) {}
  bool operator<(const job &B) const {
    return this->q<B.q;
  }
};

bool sort_comp(const job &A, const job &B) {
  return A.d<B.d;
}

int main() {
  int cas;
  cin >> cas;
  while (cas-->0) {
    int n;
    cin >> n;
    vector<job> J;
    for (int i=0; i<n; ++i) {
      int a,b;
      cin >> a >> b;
      J.push_back(job(a,b));
    }
    sort(J.begin(),J.end(),sort_comp);
    int t = 0;
    priority_queue<job> S;
    for (int i=0; i<n; ++i) {
      if (t+J[i].q <= J[i].d) {
	t += J[i].q;
	S.push(J[i]);
      }
      else if (!S.empty() && J[i].q < S.top().q) {
	t += J[i].q - S.top().q;
	S.pop();
	S.push(J[i]);
      }
    }
    cout << S.size() << endl;
    if (cas>0) cout << endl;
  }
  return 0;
}
