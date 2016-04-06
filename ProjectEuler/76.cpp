#include <iostream>
using namespace std;

/*
  cf problem 78
*/

const int M = 101;
int Q[M];

int main() {
  for (int n=0; n<M; ++n) Q[n] = 1;
  for (int m=2; m<M; ++m) {
    //cout << m-1 << " " << Q[m-1] << endl;
    for (int n=m; n<M; ++n) Q[n] = Q[n]+Q[n-m];
  }
  // n = n does not count here (hence result-1)
  cout << Q[100]-1 << endl;
  return 0;
}
