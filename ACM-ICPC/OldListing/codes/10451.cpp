#include <iostream>
#include <math.h>

using namespace std;

int main(){
  int i=1;
  double n, A, r, R, S, s, O;
  cin >> n;
  while (n>2){
    cin >> A;
    r=sqrt(A/n*(cos(M_PI/n)/sin(M_PI/n)));
    R=r/cos(M_PI/n);
    S=M_PI*( R*R    )-A;
    s=M_PI*r*r;
    O=A-s;
    
    printf("Case %d: %.5f %.5f\n", i, S, O);
    i++;
    cin >> n;
  } 
  return 0;
}
