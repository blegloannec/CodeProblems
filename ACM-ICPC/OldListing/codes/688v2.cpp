#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstdio>
using namespace std;

#define MAX 1002

typedef double flott;

struct rect {
  flott x1,y1,x2,y2;
  rect(flott x1, flott y1, flott x2, flott y2) : x1(x1),y1(y1),x2(x2),y2(y2) {};
};

vector<flott> ab,ord;
bool t[MAX][MAX];
vector<rect> rects;
map<flott,int> invabs,invord;

int reva(flott f) {
  return invabs.find(f)->second;
}

int revo(flott f) {
  return invord.find(f)->second;  
}

bool sup(flott a, flott b) {
  return a>b;
}

int main() {
  int nb,cas,k,lx,ly;
  flott x,y,r;
  vector<flott>::iterator it;
  vector<rect>::iterator itr;

  cas = 1;
  while (cin >> nb) {
    if (nb==0) return 0;
    rects.clear();
    while (nb-->0) {
      cin >> x >> y >> r;
      rects.push_back(rect(x-r,y-r,x+r,y+r));
      ab.push_back(x-r);
      ab.push_back(x+r);
      ord.push_back(y-r);
      ord.push_back(y+r);
    }

    sort(ab.begin(),ab.end());
    sort(ord.begin(),ord.end());
    
    invabs.clear();
    invord.clear();
    k = 0;
    for (it=ab.begin(); it!=ab.end(); it++) {
      invabs.insert(pair<flott,int>(*it,k));
      ++k;
    }
    lx = k;
    k = 0;
    for (it=ord.begin(); it!=ord.end(); it++) {
      invord.insert(pair<flott,int>(*it,k));
      ++k;
    }
    ly = k;
    
    for (int i=0; i<lx; i++)
      for (int j=0; j<ly; j++)
	t[i][j] = false;

    r = 0;
    for (itr=rects.begin(); itr!=rects.end(); itr++)
      for (int i=reva(itr->x1); i<reva(itr->x2); i++)
	for (int j=revo(itr->y1); j<revo(itr->y2); j++)
	  if (!t[i][j]) {
	    r += (ab[i+1]-ab[i])*(ord[j+1]-ord[j]);
	    t[i][j] = true;
	  }

    printf("%d %.2f\n",cas++,round(100*r)/100);
 
  }
  
  return 0;
}
