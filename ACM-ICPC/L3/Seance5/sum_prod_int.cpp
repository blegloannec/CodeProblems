#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

/*
double absd(double x) { // fabs existe pour les float
  if (x>=0) return x;
  else return -x;
}
*/


int main() {
  double m0,M0;
  int m,M,x,y,z,s,ymax;
  cin >> m0 >> M0;
  m = 100*m0;
  M = 100*M0;

  for (s=m; s<=M; s++) {
    ymax = s/2;
    for (x=0; x<=s/3; x++) 
      for (y=x; y<=min(ymax,(s-x)/2); y++) {
	z = s-x-y;
	if (s*1e4==x*y*z)
	  printf("%.2f = %.2f + %.2f + %.2f = %.2f * %.2f * %.2f\n",(double)s/100,(double)x/100,(double)y/100,(double)z/100,(double)x/100,(double)y/100,(double)z/100);
      }
  }
 
  return 0;
}
