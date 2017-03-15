#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// brute force, runs in 45s with -O3

const long long N = 2000000001;
vector<bool> A(N,false),B(N,false),C(N,false),D(N,false);

int main() {
  int S = (int)sqrt(N) + 1;
  for (long long a=1; a<S; ++a)
    for (long long b=1; b*b<N-a*a; ++b) {
      long long n = a*a+b*b;
      if (n<N) {
	A[n] = true;
	n = a*a+2*b*b;
	if (n<N) {
	  B[n] = true;
	  n = a*a+3*b*b;
	  if (n<N) {
	    C[n] = true;
	    n = a*a+7*b*b;
	    if (n<N) D[n] = true;
	  }
	}
      }
    }
  int cpt = 0;
  for (int a=1; a<N; ++a)
    if (A[a]&&B[a]&&C[a]&&D[a]) ++ cpt;
  cout << cpt << endl;
  return 0;
}
