// O(N^2) meet-in-the-middle a+b = d-c
// could probably be improved a lot...
#include <iostream>
#include <vector>
#include <unordered_map>
#include <climits>
#include <algorithm>
using namespace std;
using idx = short;

int N;
vector<int> S;

struct sumset {
  int total, sum;
  vector<idx> count;
  
  sumset() : total(0) {}
  
  void insert(idx i, idx j) {
    ++total;
    sum = S[i]+S[j];
    count.push_back(i);
    count.push_back(j);
  }
  
  void finalize() {
    sort(count.begin(), count.end());
  }
  
  int count_idx(idx i) {
    auto it = lower_bound(count.begin(), count.end(), i);
    if (it==count.end()) return 0;
    int l = distance(count.begin(), it);
    int r = distance(count.begin(), upper_bound(count.begin(), count.end(), i));
    return r-l;
  }
  
  int count_distinct(idx i, idx j) {
    int cnt = total - count_idx(i) - count_idx(j);
    if (S[i]+S[j]==sum) ++cnt;
    return cnt;
  }
};

unordered_map<int,sumset> AB;

void precomp() {
  for (idx ia=0; ia<N; ++ia)
    for (idx ib=ia+1; ib<N; ++ib)
      AB[S[ia]+S[ib]].insert(ia,ib);
  for (auto it=AB.begin(); it!=AB.end(); ++it)
    it->second.finalize();
}

int right_pass() {
  int maxd = INT_MIN;
  for (idx id=0; id<N; ++id)
    for (idx ic=0; ic<N; ++ic)
      if (ic!=id) {
	auto it = AB.find(S[id]-S[ic]);
	if (it!=AB.end() && it->second.count_distinct(id,ic)>0)
	  maxd = max(maxd, S[id]);
      }
  return maxd;
}

int main() {
  cin >> N;
  S.resize(N);
  for (int i=0; i<N; ++i) cin >> S[i];
  precomp();
  int d = right_pass();
  if (d==INT_MIN) cout << "no solution" << endl;
  else cout << d << endl;
  return 0;
}
