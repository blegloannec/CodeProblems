#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

#define N 101

struct point{
  double cx;
  double cy;
};

point tab[N];
int n;
double mx,my,xo,yo;

double ang(point a){
  double n1, n2, mix, sca;
  n1 = sqrt((xo-mx)*(xo-mx)+(yo-my)*(yo-my));
  n2 = sqrt((a.cx-mx)*(a.cx-mx)+(a.cy-my)*(a.cy-my)); 
  mix = ((xo-mx)*(a.cy-my)-(yo-my)*(a.cx-mx))/(n1*n2);
  sca = ((xo-mx)*(a.cx-mx)+(yo-my)*(a.cy-my))/(n1*n2);

  if ( mix > 0)
    if (sca > 0)
      return mix;
    else 
      return 2-mix;
  else{
    if (sca < 0)
      return 2- mix ; 
    else 
      return 4+ mix ;
  }
}

bool cmp(point a, point b){
  return (ang(a) < ang(b));
}

void pouet(){
  double xx,yy;
  
  for (int i=0;i<n;i++){
    cin >> xx;
    cin >> yy;
    mx = (mx*i+xx)/(i+1);
    my = (my*i+yy)/(i+1);
    tab[i].cx = xx;
    tab[i].cy = yy;
  }
  xo=tab[0].cx;
  yo=tab[0].cy;
  
  sort(tab, tab+n, cmp);
   
  // for (int i=0;i<n;i++)
  //cout << tab[i].cx << " " << tab[i].cy << endl;
    

  
  double resx=0, resy=0, c=0, a;
  
  for (int i=0;i<n;i++){
    xx = (tab[i].cx+tab[(i+1)%n].cx+mx)/3;
    yy = (tab[i].cy+tab[(i+1)%n].cy+my)/3;
    a = ((tab[i].cx-mx)*(tab[(i+1)%n].cy-my)-(tab[i].cy-my)*(tab[(i+1)%n].cx-mx))/2;
    if (a<0)
      a = -a;
    
    resx = (resx + xx*a);
    resy = (resy + yy*a);
    c = c + a;
  }
  resx = resx/c;
  resy = resy/c;
  // cout << "c= " << c << "\n";
if (resx > -0.0005 && resx <= 0)
   resx = 0;
if (resy > -0.0005 && resy <= 0)
   resy = 0;
   printf("%.3f %.3f\n", resx, resy);
  
}

int main(){
  cin >> n;
  while (n>2){
    pouet();
    cin >> n;
  }
  return 0;
}
