#include <cstdio>
#include <vector>
using namespace std;

const int N = 10000001;
vector<bool> P(N,true);
vector<int> Nbdiv(N,1);

void sieve_nb_divisors() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i]) {
      Nbdiv[i] = 2;
      for (int k=2*i; k<N; k+=i) {
	P[k] = false;
	int l = k/i;
	int j = 1;
	while (l%i==0) {
	  l /= i;
	  ++j;
	}
	Nbdiv[k] *= j+1;
      }
    }
}

int main() {
  sieve_nb_divisors();
  vector<int> C(N,0);
  for (int n=1; n<N; ++n) {
    C[n] = C[n-1];
    if (Nbdiv[n]==Nbdiv[n+1]) ++C[n];
  }
  int t,k;
  scanf("%d",&t);
  for (int i=0; i<t; ++i) {
    scanf("%d",&k);
    printf("%d\n",C[k-1]);
  }
  return 0;
}
