#include <iostream>
#include <cmath>
using namespace std;

const int C = 500000;
bool P[C];

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i<C; ++i) P[i] = true;
  for (int i=2; i<C; ++i)
    if (P[i])
      for (int j=2*i; j<C; j+=i)
	P[j] = false;
}

int main() {
  sieve();
  int conj[C];
  for (int i=0; i<C; ++i) conj[i] = 0;
  for (int i=2; i<C; ++i)
    if (P[i])
      for (int a=0; i+2*a*a<C; ++a)
	conj[i+2*a*a] += 1;
  int T,N;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    cout << conj[N] << endl;
  }
  return 0;
}
