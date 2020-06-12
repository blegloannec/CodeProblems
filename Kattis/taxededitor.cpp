// Dicho search  +  Moore-Hogdson scheduling
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
using ent = long long;

struct job {
  ent l, d;  // length/duration, deadline
  job(ent l, ent d) : l(l), d(d) {}
  bool operator<(const job &B) const {
    return l < B.l;
  }
};

int moore_hogdson(const vector<job> &J) {
  // assuming jobs are sorted by deadline
  ent t = 0;
  priority_queue<job> S;
  for (const job &j : J) {
    if (t+j.l <= j.d) {
      t += j.l;
      S.push(j);
    }
    else if (!S.empty() && j.l < S.top().l) {
      t += j.l - S.top().l;
      S.pop();
      S.push(j);
    }
  }
  return S.size();
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int N, Late;
  cin >> N >> Late;
  vector<job> J, J0;
  for (int i=0; i<N; ++i) {
    ent l, d;
    cin >> l >> d;
    J.push_back(job(l, d));
  }
  sort(J.begin(), J.end(),
       [](const job &A, const job &B) { return A.d < B.d; });
  J0 = J;
  // dicho search for the min acceptable time
  ent l = 1LL, r = 1LL<<48;
  while (l<r) {
    ent s = (l+r)/2LL;
    for (int i=0; i<N; ++i)
      J[i].d = J0[i].d * s;
    if (N-moore_hogdson(J)<=Late) r = s;
    else l = s+1;
  }
  cout << l << endl;
  return 0;
}
