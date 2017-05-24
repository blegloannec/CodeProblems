#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> couple;

int main() {
  int T,N,a,b;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    vector<couple> I;
    for (int i=0; i<N; ++i) {
      cin >> a >> b;
      I.push_back(couple(b,a));
    }
    sort(I.begin(),I.end());
    int curr = I[0].first;
    int cpt = 1;
    for (int i=1; i<N; ++i)
      if (I[i].second > curr) {
	curr = I[i].first;
	++cpt;
      }
    cout << cpt << endl;
  }
  return 0;
}
