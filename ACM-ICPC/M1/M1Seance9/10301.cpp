#include <iostream>
using namespace std;

#define SQR(X) ((X)*(X))

const int N = 100;
int n;
double X[N],Y[N],R[N];
int T[N],S[N];

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int i, int j) {
  int i0 = find(i), j0 = find(j);
  T[j0] = i0;
  S[i0] += S[j0];
}

bool inter(int i, int j) {
  double d = SQR(X[i]-X[j])+SQR(Y[i]-Y[j]);
  return (SQR(R[i]-R[j])<d && d<SQR(R[i]+R[j]));
}

int main() {
  while (true) {
    cin >> n;
    if (n<0) break;
    for (int i=0; i<n; ++i) {
      cin >> X[i] >> Y[i] >> R[i];
      T[i] = -1;
      S[i] = 1;
    }
    for (int i=0; i<n; ++i)
      for (int j=i+1; j<n; ++j)
	if (find(i)!=find(j) && inter(i,j))
	  merge(i,j);
    int M = 0;
    for (int i=0; i<n; ++i) M = max(M,S[i]);
    cout << "The largest component contains " << M << " ring" << (M!=1?"s":"") << "." << endl;
  }
  return 0;
}
