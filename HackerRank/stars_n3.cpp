/*
  "No three points lie on a line."
  the solution is then an infinitesimal rotation or translation
  of a line going through two stars 
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long ent;
int N;
vector<int> V;
vector<ent> X,Y;

bool turn_left(int i, int j, int k) {
  return (X[j]-X[i])*(Y[k]-Y[i])-(X[k]-X[i])*(Y[j]-Y[i])>0;
}

/*
  O(N^3) approach
  for each pair of points A and B, count weight on each side
  of the AB line in O(N)
*/
int solve_n3() {
  int dmin = 1<<25, wmax = 0;
  for (int i=0; i<N; ++i)
    for (int j=i+1; j<N; ++j) {
      int w1 = 0, w2 = 0;
      for (int k=0; k<N; ++k) {
	if (k==i || k==j) continue;
	if (turn_left(i,j,k)) w1 += V[k];
	else w2 += V[k];
      }
      // where do we put i and j? two cases
      if (w1>w2) swap(w1,w2);
      int v1 = V[i], v2 = V[j];
      if (v1>v2) swap(v1,v2);
      w1 += v1+v2;                 // case 1
      int w = min(w1,w2), d = abs(w1-w2);
      if (d<dmin) {
	dmin = d; wmax = w;
      }
      else if (d==dmin && w>wmax) wmax = w;
      w1 -= v1; w2 += v1;          // case 2
      w = min(w1,w2); d = abs(w1-w2);
      if (d<dmin) {
	dmin = d; wmax = w;
      }
      else if (d==dmin && w>wmax) wmax = w;
    }
  return wmax;
}

int main() {
  cin >> N;
  X.resize(N); Y.resize(N); V.resize(N);
  for (int i=0; i<N; ++i)
    cin >> X[i] >> Y[i] >> V[i];
  cout << solve_n3() << endl;
  return 0;
}
