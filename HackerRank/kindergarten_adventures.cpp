// O(n) approach (through basic "offline prefix-sum")
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> I(n,0);
  for (int i=0; i<n; ++i) {
    int t;
    cin >> t;
    if (t<n) {             // if t>=n, i is never ready
      if (t==0) ++I[0];    // i is ok on whole [0,n-1]
      else {
	++I[i+1];
	int s = i-t+1;
	if (s>=0) ++I[0];  // i is ok on [0,s-1] and [i+1,n-1]
	else s = (s+n)%n;  // i is ok on [i+1,s-1]
	--I[s];
      }
    }
  }
  int best = 0, ibest = 0, curr = 0;
  for (int i=0; i<n; ++i) {
    curr += I[i];
    if (curr>best) {
      best = curr;
      ibest = i;
    }
  }
  cout << ibest+1 << endl;
  return 0;
}
