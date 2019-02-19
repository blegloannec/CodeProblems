#include <iostream>
#include <vector>
using namespace std;

const int M = 101;
int N;
vector<int> A;
vector< vector< pair<char,int> > > DP;

void dp() {
  DP.resize(N);
  DP[0].resize(M,make_pair('#',-1));
  DP[0][A[0]%M] = make_pair('^',-1);
  for (int i=1; i<N; ++i) {
    DP[i].resize(M,make_pair('#',-1));
    for (int r=0; r<M; ++r)
      if (DP[i-1][r].first!='#') {
	DP[i][(r+A[i])%M] = make_pair('+',r);
	DP[i][(((r-A[i])%M)+M)%M] = make_pair('-',r);
	DP[i][(r*A[i])%M] = make_pair('*',r);
      }
  }
}

int main() {
  cin >> N;
  A.resize(N);
  for (int i=0; i<N; ++i) cin >> A[i];
  dp();
  int i = N-1, r = 0;
  vector<char> Op(N);
  while (i>0) {
    Op[i] = DP[i][r].first;
    r = DP[i][r].second;
    --i;
  }
  cout << A[0];
  for (int i=1; i<N; ++i) cout << Op[i] << A[i];
  cout << endl;
  return 0;
}
