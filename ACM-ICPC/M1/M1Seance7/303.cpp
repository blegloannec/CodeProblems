#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

const double H = 1.;
const double ERR = 1e-6;
const int N = 20;
int n;
double X[N],Y[N];

double xmax(double a, double b) {
  int i = 0;
  while (i<n && Y[i]-H-ERR<=a*X[i]+b && a*X[i]+b<=Y[i]+ERR) ++i;
  double x = X[0];
  if (i==n) x = X[n-1];
  else if (i>0) {
    double dy = (a*X[i]+b<Y[i]-H ? H : 0.);
    double c = (Y[i]-Y[i-1]) / (X[i]-X[i-1]);
    double d = (Y[i-1]-dy) - c*X[i-1];
    x = (d-b)/(a-c);
  }
  return x;
}

int main() {
  scanf("%d",&n);
  while (n>0) {
    for (int i=0; i<n; ++i) scanf("%lf %lf",&X[i],&Y[i]);
    double x = X[0];
    for (int i=0; i<n; ++i)
      for (int di=0; di<=1; ++di)
	for (int j=i+1; j<n; ++j)
	  for (int dj=0; dj<=1; ++dj) {
	    double a = ((Y[j]-dj*H)-(Y[i]-di*H)) / (X[j]-X[i]);
	    double b = (Y[i]-di*H) - a*X[i];
	    x = max(x,xmax(a,b));
	  }
    if (x>=X[n-1]) printf("Through all the pipe.\n");
    else printf("%.2lf\n",round(100.*x)/100.);
    scanf("%d",&n);
  }
  return 0;
}
