/* Algo en n^3
   On pourrait faire mieux (proche n^2 en pratique)
   en travaillant sur des carrés 5x5 cm, mais c'est
   chiant à coder.
*/

#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

#define MAX 202
#define RAY 2.5
#define RANGE 1e-16
#define MOY(X,Y) (((X)+(Y))/2.0)
#define NORM(X,Y) sqrt((X)*(X)+(Y)*(Y))
#define NORM2(X,Y) ((X)*(X)+(Y)*(Y))

typedef long double flott;

flott pts[MAX][2];
int n;

int main() {
  int nb,res,M1,M2;
  flott x,y,x2,y2,mx,my,d,vx,vy,cx1,cy1,cx2,cy2,svg,vn;
  char buff[100];

  cin >> nb;
  cin.getline(buff,sizeof(buff));
  cin.getline(buff,sizeof(buff));
  
  while (nb-->0) {

    n = 0;
    res = 0;

    cin.getline(buff,sizeof(buff));
    /* Attention
       %Lf pour des long double
       %lf pour des double
       %f pour des float
    */
    while (sscanf(buff,"%Lf %Lf",&x,&y) == 2) {
      pts[n][0] = x;
      pts[n++][1] = y;
      cin.getline(buff,sizeof(buff));
    }
    
    if (n==0) break;

    for (int i = 0; i<n-1; i++) {
      x = pts[i][0];
      y = pts[i][1];
      for (int j = i+1; j<n; j++) {
	x2 = pts[j][0];
	y2 = pts[j][1];
	if (NORM2(x2-x,y2-y)>4*RAY*RAY+RANGE) continue;
	mx = MOY(x,x2);
	my = MOY(y,y2);
	vx = mx-x;
	vy = my-y;
	vn = NORM2(vx,vy);
	d = sqrt(RAY*RAY-vn);
	vn = sqrt(vn);
	svg = vx;
	vx = (d*vy)/vn;
	vy = -(d*svg)/vn;
	
	cx1 = mx+vx;
	cy1 = my+vy;
	cx2 = mx-vx;
	cy2 = my-vy;
	M1 = 2;
	M2 = 2;
	for (int k=0; k<n; k++) {
	  if ((k==i)||(k==j)) continue;
	  if (NORM2(pts[k][0]-cx1,pts[k][1]-cy1)<=RAY*RAY+RANGE) ++M1;
	  if (NORM2(pts[k][0]-cx2,pts[k][1]-cy2)<=RAY*RAY+RANGE) ++M2;
	}
	res = max(M1,max(M2,res));
	  
      }
    }

    cout << res << '\n';

  }

  return 0;
}
