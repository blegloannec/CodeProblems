#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const double INF = 1e12;

int N,S;
vector<int> X,Y,T;
double Vm;
vector< vector<double> > Dist;

// Held-Karp-like DP (forward iterative implementation)
bool cat(double v0) {
  vector< vector<double> > DP(N, vector<double>(S, INF));
  // init.
  for (int l=0; l<N; ++l) {
    double t = hypot(X[l],Y[l])/v0;
    if (t<T[l]) DP[l][1<<l] = t;
  }
  // dp.
  for (int s=1; s<S; ++s) {
    double v = v0;
    for (int e=0; e<N; ++e)
      if ((s>>e)&1)
	v *= Vm;
    for (int l=0; l<N; ++l)
      if (DP[l][s]<INF)
	for (int k=0; k<N; ++k)
	  if (((s>>k)&1)==0) {
	    double t = DP[l][s] + Dist[l][k]/v;
	    int sk = s|(1<<k);
	    if (t<=T[k] && t<DP[k][sk])
	      DP[k][sk] = t;
	  }
  }
  // final check
  for (int l=0; l<N; ++l)
    if (DP[l].back()<INF)
      return true;
  return false;
}

int main() {
  cin >> N;
  S = 1<<N;
  X.resize(N);
  Y.resize(N);
  T.resize(N);
  for (int i=0; i<N; ++i)
    cin >> X[i] >> Y[i] >> T[i];
  cin >> Vm;
  // pre-computing distances
  Dist.resize(N, vector<double>(N));
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j)
      Dist[i][j] = hypot(X[i]-X[j], Y[i]-Y[j]);
  // dicho. search for the min speed
  double vmin = 0., vmax = 1e6;
  while (vmax-vmin>1e-4) {
    double v = (vmin+vmax)/2.;
    if (cat(v)) vmax = v;
    else vmin = v;
  }
  printf("%.3f\n", vmin);
  return 0;
}
