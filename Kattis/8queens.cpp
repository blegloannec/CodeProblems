#include <iostream>
#include <vector>
using namespace std;

const int N = 8;

bool valid_board() {
  char c;
  int n = 0;
  vector<bool> L(N,false), C(N,false), D(2*N-1,false), A(2*N-1,false);
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j) {
      cin >> c;
      if (c=='*') {
	++n;
	if (L[i] || C[j] || D[i+j] || A[i-j+N-1]) return false;
	L[i] = C[j] = D[i+j] = A[i-j+N-1] = true;
      }
    }
  return n==N;
}

int main() {
  if (valid_board()) cout << "valid" << endl;
  else cout << "invalid" << endl;
  return 0;
}
