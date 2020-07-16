#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> H;

int pass() {
  int res = 0, high = 0, dh = 0;
  for (int i=0; i<N; ++i) {
    if (H[i]>=H[high]) {
      res = max(res, dh);
      dh = 0;
      high = i;
    }
    else dh = max(dh, H[high]-H[i]);
  }
  return res;
}

int main() {
  scanf("%d", &N);
  H.resize(N);
  for (int i=0; i<N; ++i) scanf("%d", &H[i]);
  int res = pass();
  reverse(H.begin(), H.end());
  res = max(res, pass());
  printf("%d\n", res);
  return 0;
}
