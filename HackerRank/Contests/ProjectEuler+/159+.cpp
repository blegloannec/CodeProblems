#include <iostream>
#include <vector>
using namespace std;

const int N = 10000001;
vector<int> DRS(N);

int digit_root(int n) {
  return 1+((n-1)%9);
}

void sieve_drs() {
  DRS[1] = 0;
  for (int i=2; i<N; ++i) DRS[i] = digit_root(i);
  for (int i=2; i*i<N; ++i)
    for (int k=2*i; k<N; k+=i)
      DRS[k] = max(DRS[k],DRS[k/i]+DRS[i]);
}
	
int main() {
  int T,n;
  sieve_drs();
  for (int n=2; n<N; ++n) DRS[n] += DRS[n-1];
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> n;
    cout << DRS[n] << endl;
  }
  return 0;
}
