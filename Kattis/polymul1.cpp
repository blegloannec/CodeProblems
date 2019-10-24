#include <cstdio>
#include <vector>
using namespace std;

typedef vector<int> poly;

int N;
vector<int> A;

void mul(const poly &A, const poly &B, poly &C) {
  C.resize(A.size()+B.size()-1,0);
  for (unsigned int i=0; i<A.size(); ++i)
    for (unsigned int j=0; j<B.size(); ++j)
      C[i+j] += A[i] * B[j];
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; ++t) {
    int N;
    scanf("%d", &N); ++N;
    poly A(N);
    for (int i=0; i<N; ++i) scanf("%d", &A[i]);
    scanf("%d", &N); ++N;
    poly B(N);
    for (int i=0; i<N; ++i) scanf("%d", &B[i]);
    poly P;
    mul(A,B,P);
    while (P.size()>1 && P.back()==0) P.pop_back();
    int d = P.size() - 1;
    printf("%d\n", d);
    for (int i=0; i<=d; ++i)
      printf((i==d ? "%d\n" : "%d "), P[i]);
  }
  return 0;
}
