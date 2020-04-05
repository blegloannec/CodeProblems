#include <iostream>
using namespace std;

#define PMAX 1001
int N,C,I,P;
int prix2num[PMAX];

int main() {
  int sol1, sol2;
  cin >> N;
  for (int n=1; n<=N; ++n) {
    for (int i=0; i<PMAX; ++i) prix2num[i] = -1;
    cin >> C >> I;
    for (int i=1; i<=I; ++i) {
      cin >> P;
      if (prix2num[P]>0) {// prix dejà attribué
	if (C==2*P) {sol2 = i; sol1 = prix2num[P];}
      }
      else {
	if (P<C && prix2num[C-P]>0) {sol2 = i; sol1 = prix2num[C-P];}
	prix2num[P] = i;
      }
    }
    cout << "Case #" << n << ": " << sol1 << " " << sol2 << endl;
  }
  return 0;
}
