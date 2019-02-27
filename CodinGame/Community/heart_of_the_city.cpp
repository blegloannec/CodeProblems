#include <iostream>
using namespace std;

const int NMAX = 5000001;
int N;
bool P[NMAX];
int Euler[NMAX];

void sieve_euler() {
  for (int i=0; i<=N; ++i) {
    P[i] = true;
    Euler[i] = i;
  }
  for (int i=2; i<=N; ++i)
    if (P[i]) {
      Euler[i] = i-1;
      for (int k=2*i; k<=N; k+=i) {
	P[k] = false;
	Euler[k] = (Euler[k]/i)*(i-1);
      }
    }
}

int main() {
  cin >> N;
  N >>= 1;
  sieve_euler();
  long long S = 0;
  for (int i=2; i<=N; ++i) S += Euler[i];
  S = 8*(S+1);
  cout << S << endl;
  return 0;
}
