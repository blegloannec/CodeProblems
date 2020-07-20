#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

typedef int answers;       // M answers bitmask
typedef long long grades;  // tuple of N half-grades

int N, M;
vector<answers> A;
vector<int> G;
grades full;

int grade(answers a, answers b, int s) {
  int g = 0;
  for (int i=0; i<s; ++i) {
    if ((a&1)==(b&1)) ++g;
    a >>= 1; b >>= 1;
  }
  return g;
}

int meet_in_the_middle(answers &sol) {
  // computing and hashing first half-grades
  unordered_map<grades, vector<answers> > HG1;
  int M1 = M/2; int M2 = M-M1;
  for (answers a1=0; a1<(1<<M1); ++a1) {
    grades hg1 = 0;
    bool valid = true;
    for (int i=0; i<N && valid; ++i) {
      int g = grade(a1, A[i], M1);
      if (G[i]-M2<=g && g<=G[i])
	hg1 |= ((grades)g)<<(5*i);
      else valid = false;
    }
    if (valid)
      HG1[hg1].push_back(a1);
  }
  // second half
  int cnt = 0;
  for (answers a2=0; a2<(1<<M2); ++a2) {
    grades hg2 = 0;
    bool valid = true;
    for (int i=0; i<N && valid; ++i) {
      int g = grade(a2, A[i]>>M1, M2);
      if (G[i]-M1<=g && g<=G[i])
	hg2 |= ((grades)g)<<(5*i);
      else valid = false;
    }
    if (valid) {
      grades hg1 = full - hg2;
      auto it = HG1.find(hg1);
      if (it!=HG1.end()) {
	if (cnt==0)  // first solution
	  sol = it->second[0] | (a2<<M1);
	cnt += it->second.size();
      }
    }
  }
  return cnt;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N >> M;
    A.resize(N);
    G.resize(N);
    full = 0;
    for (int i=0; i<N; ++i) {
      string S;
      cin >> S >> G[i];
      A[i] = 0;
      for (int j=0; j<M; ++j)
	if (S[j]=='1')
	  A[i] |= 1<<j;
      full |= ((grades)G[i])<<(5*i);
    }
    answers sol;
    int cnt = meet_in_the_middle(sol);
    if (cnt==1) {
      for (int i=0; i<M; ++i) {
	cout << (sol&1);
	sol >>= 1;
      }
      cout << endl;
    }
    else cout << cnt << " solutions" << endl;
  }
  return 0;
}
