#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/*
  Recursive memoized computation of E in O(2^n) with n<=29
  Several optimizations are required to speed up things:
   - use bitmasks to represent words and
   - use two different structures to store memoized results:
      - linear array (mask -> result) of size 2^s for words of
        size s when s is small enough
	(the space of masks is small enough and we potentially
	 explore a large amount of these words so the benefit of
	 array access is significant)
      - hashtable for words of large size
        (the space of masks is too large for an array and we explore
	 a relatively small amount of these words so the hashtable
	 overcost is not too bad)
  NB (a posteriori): The editorial uses the same approach exactly,
                     no smart insight to find here.
*/

int s0;
const int upper_size = 30;
const int memo_thresh = 23;
vector< vector<double> > memo1(memo_thresh+1);
vector< unordered_map<int,double> > memo2(upper_size);

int cut(int w, int k) {
  return (w&((1<<k)-1)) | ((w>>(k+1))<<k);
}

double E(int s, int w) {
  if (s==s0) return 0.;
  if (s<=memo_thresh && memo1[s][w]>=0.) return memo1[s][w];
  else if (s>memo_thresh && memo2[s].find(w)!=memo2[s].end()) return memo2[s][w];
  double e = 0.;
  for (int i=0; i<s/2; ++i) {
    int j = s-1-i;
    e += 2.*max(E(s-1,cut(w,i))+((w>>i)&1), E(s-1,cut(w,j))+((w>>j)&1));
  }
  if ((s&1)==1) {
    int i = s/2;
    e += E(s-1,cut(w,i))+((w>>i)&1);
  }
  e /= s;
  if (s<=memo_thresh) memo1[s][w] = e;
  else memo2[s][w] = e;
  return e;
}

int main() {
  int N,K;
  cin >> N >> K;
  s0 = N-K;
  string W;
  cin >> W;
  int w = 0;
  for (int i=0; i<N; ++i) w |= (W[i]=='W')<<i;
  for (int s=s0+1; s<=min(N,memo_thresh); ++s) memo1[s].resize(1<<s, -1.);
  double res = 0.;
  if (K==N)
    for (int i=0; i<N; ++i) res += (W[i]=='W');
  else res = E(N,w);
  printf("%.9lf\n", res);
  return 0;
}
