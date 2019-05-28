#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const int MIN = 100000000;
const int N   = 100000;

struct point {
  double cx,cy;
  point(double cx=0., double cy=0.) : cx(cx), cy(cy) {}
};

int n;
point x[N];

bool cmpx(const point &a, const point &b) {
  return a.cx > b.cx;
}

bool cmpy(const point &a, const point &b) {
  return a.cy > b.cy;
}

double dist(const point &a, const point &b) {
  return (a.cx-b.cx)*(a.cx-b.cx)+(a.cy-b.cy)*(a.cy-b.cy);
}

double aux(int deb, int fin) {
  double mini = MIN+1;
  if ((fin-deb)<4) {
    for (int i=deb; i<fin; ++i)
      for (int j=i+1; j<fin; ++j)
	mini = min(mini, dist(x[i],x[j]));
  }
  else {
    int mid = (fin+deb)/2;
    double l = x[mid].cx;
    int tl = 0;
    point yy[fin-deb];
    mini = min(aux(deb,mid), aux(mid,fin));
    for (int i=deb; i<fin; ++i){
      if ((x[i].cx-l)*(x[i].cx-l)<=mini)
	yy[tl++] = x[i];
    }
    stable_sort(yy, yy+tl, cmpx);
    for (int i=0; i<tl; ++i)
      for (int j=i+1; j<i+7 && j<tl; ++j)
	mini = min(mini, dist(yy[i],yy[j]));
  }
  return mini;
}

int main() {
  scanf("%d", &n);
  while (n!=0) {
    double a,b;
    for (int i=0; i<n; ++i) {
      scanf("%lf %lf", &a, &b);
      x[i] = point(a,b);
    }
    sort(x, x+n, cmpx);
    double res = aux(0,n);
    if (res <= MIN) printf("%.4f\n", sqrt(res));
    else printf("INFINITY\n");
    scanf("%d", &n);
  }
  return 0;
}
