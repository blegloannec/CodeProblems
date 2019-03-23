#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> H(N);
  for (int i=0; i<N; ++i) cin >> H[i];
  long long res = 0;
  stack< pair<int,int> > S; // (previous greater height, multiplicity) stack
  for (int i=0; i<N; ++i) {
    while (!S.empty() && H[S.top().first]<H[i]) S.pop();
    // if(...) then S.top().second contains the valid routes ending in i
    if (!S.empty() && H[S.top().first]==H[i]) res += 2 * S.top().second++;
    else S.push(make_pair(i,1));
  }
  cout << res << endl;
  return 0;
}
