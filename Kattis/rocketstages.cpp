#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
using ll = long long;

/*
  O(N*M) DP
  v'(t) = T / m(t) - g
  stage is working during L/C s
  m(t) = m0 + S + L - tC  where m0 is the mass of all remaining stages
  v(t) = v0 + Integral( T/m(t)-g, t=0..L/C )
       = v0 - T/C (ln m(0) - ln m(0)) - gL/C
*/

const double g = 9.8;
const int M = 10000;

int main() {
  int N;
  scanf("%d", &N);
  vector<double> V(M+1,0.);  // max speed achievable for each total mass
  for (int i=0; i<N; ++i) {
    ll S,L; double T,C;
    scanf("%lld %lld %lf %lf", &S, &L, &T, &C);
    for (ll m0=M-(S+L); m0>=0; --m0) { // /!\ start from the highest mass!
      if (T>=g*(m0+S+L)) {
	double v = V[m0] - T/C*(log(m0+S) - log(m0+S+L)) - g*L/C;
	V[m0+S+L] = max(V[m0+S+L], v);
      }
    }
  }
  ll res = 0;
  for (double v : V) res = max(res, (ll)round(v));
  printf("%lld\n", res);
  return 0;
}
