#include <iostream>
#include <math.h>

using namespace std;

int main(){
  double n, r, t, a, ai;
  while (cin >> r){
    cin >> n;
    a = (M_PI)/(n);
    t = 2*r*sin(a);
    ai = ((n*t*t)/(4*tan(M_PI/n)));
    printf("%.3f\n", ai);
  } 
  return 0;
}
