#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int cas,N,A,B,hA,hB,h;
  cin >> cas;

  while (cas-->0) {
    cin >> N >> A >> B;
    hA = (int)floor(log((double)A)/log(2.));
    hB = (int)floor(log((double)B)/log(2.));
    h = max(hA,hB);
    cout << (int)pow(2.,(double)N)-(int)pow(2.,(double)N-(double)h)+1 << endl;
  }

  return 0;
}
