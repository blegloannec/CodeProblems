#include <iostream>
#include <vector>
using namespace std;

// can't pass that in python...

typedef long long ent;
const ent inf = 1LL<<50;
int H,N;
vector<ent> W;

int max_possible_height() {
  ent w = 1, s = 0;
  int h = 0;
  while (w<=1000000000) {
    if (s<=6*w) {
      ++h;
      s += w;
    }
    else w = (s+5)/6;
  }
  return h;
}

// DP_i[h] = min weight of a tower of size h using the ants < i
int dp() {
  vector<ent> DPi(H+1,inf);
  DPi[0] = 0;
  for (int i=0; i<N; ++i) {
    vector<ent> DPi1 = DPi;
    for (int h=1; h<=H; ++h) {
      if (DPi[h-1]<=6*W[i]) DPi1[h] = min(DPi1[h],DPi[h-1]+W[i]);
      if (DPi1[h]==inf) break;
    }
    DPi = DPi1;
  }
  int h = H;
  while (DPi[h]==inf) --h;
  return h;
}

int main() {
  H = max_possible_height();  // 139
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cin >> N;
    W.resize(N);
    for (int i=0; i<N; ++i) cin >> W[i];
    cout << "Case #" << t << ": " << dp() << endl;
  }
  return 0;
}
