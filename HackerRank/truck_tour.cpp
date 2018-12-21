/*
  O(n) calculation-based solution here
  NB: The editorial uses a nice insight that simplifies things a little!
      If, when starting at i, the cumulative sum (S[] in this code) becomes
      negative for the first time at j, then it would also become negative
      at most at j when starting at any point within [i,j].
      Hence we only have to naively simulate from any i, simply skipping
      those eliminated intervals of starting values. This leads to a simpler,
      still O(n), and more elegant solution.
*/
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef long long ent;
int N;
vector<ent> P;

int min_tour_start() {
  vector<ent> S = P;
  for (int i=1; i<N; ++i) S[i] += S[i-1];
  vector<ent> M = S;
  for (int i=N-2; i>=0; --i) M[i] = min(S[i],M[i+1]);
  if (M[0]>=0) return 0;  // starting at 0
  ent Sloop = S.back(), Mloop = 1LL<<60;
  for (int i=1; i<N; ++i) {  // starting at i
    Sloop += P[i-1];  // cumulative sum of 1 full turn + [0..i-1]
    Mloop = min(Mloop,Sloop);  // min of the part 1 full turn + [0..i-1]
    // M[i] is the min of S[i..N-1]
    // we want the min of the part [i..N-1,0..i-1] = min(M[i],Mloop)
    // as we use cumulative sum, all values are shifted by S[i-1]
    if (min(M[i],Mloop)-S[i-1]>=0) return i;
  }
  assert(false);  // no solution, should not happen here
  return -1;
}

int main() {
  cin >> N;
  P.resize(N);
  for (int i=0; i<N; ++i) {
    ent p,d;
    cin >> p >> d;
    P[i] = p-d;
  }
  cout << min_tour_start() << endl;
  return 0;
}
