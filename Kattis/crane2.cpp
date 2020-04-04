#include <cstdio>
#include <vector>
using namespace std;

typedef pair<int,int> itv;  // even interval

int N;
vector<int> A;

// sort in O(N log N) operations
// overall simulation in O(N^2 log N)
vector<itv> crane_sort() {
  vector<itv> Moves;
  while (N>1) {
    // find N (current max)
    int l = 0;
    while (A[l]!=N) ++l;
    // move it to the end in O(log N) operations
    while (l<N-1) {
      int r = N;
      if ((r-l)%2!=0) --r;
      Moves.push_back(make_pair(l+1,r));
      int m = (l+r)/2;
      while (m<r) swap(A[l++], A[m++]);
    }
    --N;
  }
  return Moves;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t=0; t<T; ++t) {
    scanf("%d", &N);
    A.resize(N);
    for (int i=0; i<N; ++i) scanf("%d", &A[i]);
    auto Moves = crane_sort();
    printf("%ld\n", Moves.size());
    for (const auto &M : Moves)
      printf("%d %d\n", M.first, M.second);
  }
  return 0;
}
