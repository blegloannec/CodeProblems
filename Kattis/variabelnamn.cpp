#include <cstdio>
#include <vector>
#include <unordered_set>
using namespace std;

const int NSUP = 10001;

int main() {
  int N;
  scanf("%d", &N);
  vector<int> M(NSUP);
  for (int i=0; i<NSUP; ++i) M[i] = i;
  unordered_set<int> used;
  for (int i=0; i<N; ++i) {
    int x;
    scanf("%d", &x);
    while (used.find(M[x])!=used.end()) M[x] += x;
    printf("%d\n", M[x]);
    used.insert(M[x]);
    M[x] += x;
  }
  return 0;
}
