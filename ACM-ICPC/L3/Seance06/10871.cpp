#include <iostream>
using namespace std;

const int N = 1001;  // this is actually good enough, even though according to
                     // the statement this should be 10001 (which passes too)
const int M = N*N+1;
int n;
int A[N],S[N];
bool P[M];

void sieve() {
  P[0] = P[1] = false;
  fill(P+2,P+M,true);
  for (int i=2; i<M; ++i)
    if (P[i])
      for (int k=2*i; k<M; k+=i)
	P[k] = false;
}

void primed() {
  for (int l=2; l<=n; ++l)
    for (int i=1; i+l-1<=n; ++i)
      if (P[S[i+l-1]-S[i-1]]) {
	cout << "Shortest primed subsequence is length " << l << ":";
	for (int j=i-1; j<i+l-1; ++j) cout << ' ' << A[j];
	cout << endl;
	return;
      }
  cout << "This sequence is anti-primed." << endl;
}

int main() {
  S[0] = 0;
  sieve();
  int t;
  cin >> t;
  while (t--) {
    cin >> n;
    for (int i=0; i<n; ++i) {
      cin >> A[i];
      S[i+1] = S[i]+A[i];  // prefix sums
    }
    primed();
  }
  return 0;
}
