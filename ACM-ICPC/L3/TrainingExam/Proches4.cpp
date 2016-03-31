#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

struct point{
  int x;
  int y;
}; 
bool supx (point a, point b){
  return (a.x > b.x) || ((a.x == b.x) && (a.y > b.y)); }
bool supy (point a, point b){
  return (a.y > b.y) || ((a.y == b.y) && (a.x > b.x)); }
int dist_carre(point a, point b){
  return (a.x-b.x)*(a.x-b.x) + (a.y - b.y)*(a.y - b.y); }


int traite_en_y(point vx[], int nb, point vy[]);


int traite_en_x(point vx[], int nb, point vy[]){
  if (nb <= 1) return 0;
  if (nb == 2) return dist_carre(vx[1], vx[2]);
  if (nb == 3) {
    int d1 = dist_carre(vx[1],vx[2]);
    int d2 = dist_carre(vx[1],vx[3]);
    int d3 = dist_carre(vx[2],vx[3]);
    return min(min(d1,d2),d3);
  }

  int med = nb / 2;
  point v1x[med+1]; 
  point v2x[med+2];
  int tv1x = med;
  int tv2x = med + (nb % 2);
  for (int i = 1; i <= nb; ++i){
    if (i <= med) v1x[i] = vx[i];
    else v2x[i - med] = vx[i];
  }
  
  point v1y[med+1];
  point v2y[med+2];
  int tv1y = 0;
  int tv2y = 0;
  point valmed = vx[med];
  for(int i = 1; i <= nb; ++i){
    if (supx(vy[i],valmed)) {tv2y++; v2y[tv2y] = vy[i];}
    else {tv1y++; v1y[tv1y] = vy[i];};
  }
  if((tv1y != med)||(tv2y != med + (nb % 2))) cout << "ERREUR !!!" << tv1y << " " << tv2y << " " << med << endl;

  
  int dist1 = traite_en_y(v1x,med,v1y);
  int dist2 = traite_en_y(v2x,med+(nb%2),v2y);


  point proches[nb];
  int tproches = 0;
  int monmin = min(dist1, dist2);
  //if (monmin == 0) monmin = max(dist1, dist2); //cas où 1 sous routine renvoie 0. EN pratique ça n'arrive pas car les doublons sont éliminés.
  for(int i = 1; i <= nb; ++i){
    point tp = vy[i];
    if ((tp.x - valmed.x)*(tp.x - valmed.x) <= (2*monmin)) 
    {
      tproches++;
      proches[tproches] = tp;
    }
  }
  if (tproches < 6){
    for (int i = 1; i <= tproches; ++i)
      {
	for(int j = i+1; j <= tproches; ++j)
	  {
	    int d1 = dist_carre(proches[i],proches[i+j]);
	    if((d1 > 0) && (d1 < monmin)) monmin = d1;	    
	  }
      }
  }
  for(int i = 1; i <= tproches-5; ++i)
    {
      for(int j = 1; j <= 6; ++j)
	{
	  int d1 = dist_carre(proches[i],proches[i+j]);
	  if((d1 > 0) && (d1 < monmin)) monmin = d1;
	}
    }
  return monmin;
}



int traite_en_y(point vx[], int nb, point vy[]){

  if (nb <= 1) return 0;
  if (nb == 2) return dist_carre(vx[1], vx[2]);
  if (nb == 3) {
    int d1 = dist_carre(vx[1],vx[2]);
    int d2 = dist_carre(vx[1],vx[3]);
    int d3 = dist_carre(vx[2],vx[3]);
    return min(min(d1,d2),d3);
  }

  int med = nb / 2;

  point v1y[med+1]; 
  point v2y[med+2];
  int tv1y = med;
  int tv2y = med + (nb % 2);

  for (int i = 1; i <= nb; ++i){
    if (i <= med) v1y[i] = vy[i];
    else v2y[i - med] = vy[i];
  }
  
  point v1x[med+1];
  point v2x[med+2];
  int tv1x = 0;
  int tv2x = 0;
  point valmed = vy[med];
  for(int i = 1; i <= nb; ++i){
    if (supy(vx[i],valmed)) {tv2x++; v2x[tv2x] = vx[i];} 
    else {tv1x++; v1x[tv1x] = vx[i];};
  }
  if((tv1x != med)||(tv2x != med + (nb % 2))) cout << "ERREUR !!!";
  
  int dist1 = traite_en_x(v1x,med,v1y);
  int dist2 = traite_en_x(v2x,med+(nb%2),v2y);

  point proches[nb];
  int tproches = 0;
  int monmin = min(dist1, dist2);
  //if (monmin == 0) monmin = max(dist1, dist2);
  for(int i = 1; i <= nb; ++i){
    point tp = vx[i];
    if ((tp.y - valmed.y)*(tp.y - valmed.y) <= (2*monmin)) 
    {
      tproches++;
      proches[tproches] = tp;
    }
  }
  if (tproches < 6){
    for (int i = 1; i <= tproches; ++i)
      {
	for(int j = i+1; j <= tproches; ++j)
	  {
	    int d1 = dist_carre(proches[i],proches[i+j]);
	    if((d1 > 0) && (d1 < monmin)) monmin = d1;	    
	  }
      }
  }
  for(int i = 1; i <= tproches-5; ++i)
    {
      for(int j = 1; j <= 6; ++j)
	{
	  int d1 = dist_carre(proches[i],proches[i+j]);
	  if((d1 > 0) && (d1 < monmin)) monmin = d1;
	}
    }
  return monmin;
}

int main(void){
  int n;
  cin >> n;
  while(n > 0){
    vector<point> entreex;
    vector<point> entreey;
    int a,b;
    for(int i = 1; i <= n; ++i)
      {
	cin >> a >> b;
	point z;
	z.x = a;
	z.y = b;
	entreex.push_back(z);
	entreey.push_back(z);
      }
    sort(entreex.begin(), entreex.end(), supx);
    sort(entreey.begin(), entreey.end(), supy);
    
    point vx[n+1];
    point vy[n+1];
    
    for(int i = 1; i <= n; ++i)
      {
	vx[i] = entreex.back();
	entreex.pop_back();
	vy[i] = entreey.back();
	entreey.pop_back();
      }
    for(int i = 1; i <= (n-1); ++i)
      {
	point za = vx[i];
	point zb = vx[i+1];
	if((za.x == zb.x) && (za.y == zb.y)) {cout << 0 << endl; return 0;}; //élimiine les doublons. 
      }
    int res = traite_en_x(vx, n, vy);
    //cout << res << endl; //Attention, je rends un carré !
    if (res>100000000) cout << "INFINITY\n";
    else printf("%.4f\n",sqrt(res));
    
    cin >> n;
  }
  return 0;
}
