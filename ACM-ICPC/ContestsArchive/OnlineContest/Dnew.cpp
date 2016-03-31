#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

#define INF 1000000005

struct paire{
  int x;
  int y;
};

struct triple{
  int x;
  int y;
  double angl;
};

vector<paire> tab;
vector<triple> tabres;
int N;
paire mini;
double centrex, centrey;
double x1;
double yy1;
int nb;

double angles(paire p){
  double x2, y2;
  x2= p.x - centrex;
  y2= p.y - centrey;
  double norm= sqrt(x2*x2+y2*y2);
  x2= x2/norm;
  y2= y2/norm;

  double mix= x1*y2-yy1*x2;
  double sca= x1*x2+yy1*y2;

  if ( mix >= 0)
    if (sca >= 0)
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

bool cmp(triple a, triple b){
  return a.angl< b.angl;
}

int main(){
  int cas;
  cin >> cas;
  while(cas-->0){
    tab.clear();
    tabres.clear();
    mini.x= INF;
    mini.y= INF;
    centrex=0;
    centrey=0;
    nb=0;
    cin >> N;
    int x, y;
    char tmp;
    for (int i=0; i<N; ++i){
      cin >> x >> y >> tmp;
      if (tmp=='Y'){
	centrex+= x;
	centrey+= y;
	nb++;
	if (x<mini.x || (x==mini.x && y<mini.y)){
	  mini.x= x;
	  mini.y= y;
	}
	paire add;
	add.x= x;
	add.y= y;
	tab.push_back(add);
      }
    }
    centrex= centrex/nb;
    centrey= centrey/nb;
    x1= mini.x - centrex;
    yy1= mini.y - centrey;
    double norm= sqrt(x1*x1+yy1*yy1);
    x1= x1/norm;
    yy1= yy1/norm;
    for (int i=0; i<nb;++i){
      triple zoubon;
      zoubon.x= tab[i].x;
      zoubon.y= tab[i].y;
      zoubon.angl= angles(tab[i]);
      tabres.push_back(zoubon);
    }
    sort(tabres.begin(), tabres.end(), cmp);
    cout << nb << '\n';
    for (int i=0;i<nb;++i)
      cout << tabres[i].x << ' ' << tabres[i].y << '\n';
  }
}
