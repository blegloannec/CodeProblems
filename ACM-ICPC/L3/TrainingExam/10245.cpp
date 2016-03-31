#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

#define MIN 100000000
#define N 100000

typedef struct
{
  double cx;
  double cy; 
} point;

int n;
point x[N];


bool cmpx( point a, point b ) {
   return a.cx > b.cx;
 }  

bool cmpy( point a, point b ) {
   return a.cy > b.cy;
 }  

double dist(point a, point b){
  return ((a.cx-b.cx)*(a.cx-b.cx)+(a.cy-b.cy)*(a.cy-b.cy));
}

double aux(int deb, int fin){
  double mini = MIN+1;
  if ((fin-deb)<4){
    for (int i=deb;i<fin;i++)
      for (int j=i+1;j<fin;j++)
	mini = min(mini, dist(x[i], x[j]));
    return mini;
  }
  else {
    int mid = (fin+deb)/2;
    double l = x[mid].cx;
    int tl = 0;
    point yy[fin-deb];
   
    mini = min( aux(deb, mid), aux(mid, fin));
    
    for (int i=deb;i<fin;i++){
      if (((x[i].cx-l)*(x[i].cx-l))<=mini){
	yy[tl] = x[i];
	tl++;
      }
    }	   
    stable_sort( yy, yy + tl, cmpx ); 
    for (int i=0;i<tl;i++){
      for (int j=i+1;j<i+7 && j<tl;j++){
	mini = min(mini,dist(yy[i],yy[j]));
      }
    } 

    return mini; 
  }
}

void paf(){
  double a,b;
  point p;
  for (int i=0;i<n;i++){
    cin >> a >> b;
    p.cx = a;
    p.cy = b;
    x[i] = p;
    }
  sort( x, x + n, cmpx );   
  double res =  aux(0, n);
  if (res <= MIN) 
    printf("%.4f\n", sqrt(res));
    else
      cout << "INFINITY\n";
}


int main(){
  cin >> n;
  while (n!=0){
    paf();
    cin >> n;
  }
  return 0;
}
