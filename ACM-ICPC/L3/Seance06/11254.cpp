#include <iostream>
#include <cmath>
using namespace std;

void aux(int n) {
  bool h = false;
  int l = sqrt(2*n)+2, tmp = 0, tmp1;
   while (l>0 && !h) {
     --l;
     tmp = (2*n-l*(l+1))/(2*(l+1));
     h = (tmp>=0 && n==(l+1)*tmp+(l*(l+1)/2));
   }
   if (tmp==0 && l>0) tmp1 = tmp+1;
   else tmp1 = tmp;
   cout << n << " = " << tmp1 << " + ... + " << tmp+l << endl;
}

int main() {
  int n;
  cin >> n;
  while (n>=0){
    aux(n);
    cin >> n;
  }
  return 0;
}
