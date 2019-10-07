#include <cstdio>
#include <vector>
#include <set>
using namespace std;

int main() {
  int N,M,C;
  scanf("%d %d %d", &N, &M, &C);
  if (M>N) {
    printf("NONE\n");
    return 0;
  }
  vector<int> A(N), Out;
  for (int i=0; i<N; ++i) scanf("%d", &A[i]);
  multiset<int> W;
  for (int i=0; i<N; ++i) {
    if ((int)W.size()==M) W.erase(W.find(A[i-M]));
    W.insert(A[i]);
    if ((int)W.size()==M && *W.rbegin() - *W.begin() <= C) Out.push_back(i-M+1);
  }
  if (Out.empty()) printf("NONE\n");
  else for (int o : Out) printf("%d\n", o+1);
  return 0;
}
