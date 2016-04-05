#include <iostream>
#include <cmath>
using namespace std;

const int C = 100000;
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
  bool conj[C];
  for (int i=0; i<C; ++i) conj[i] = false;
  for (int i=2; i<C; ++i)
    if (P[i])
      for (int a=0; i+2*a*a<C; ++a)
	conj[i+2*a*a] = true;
  int sol = 9;
  while (conj[sol]) sol += 2;
  cout << sol << endl;
  return 0;
}
