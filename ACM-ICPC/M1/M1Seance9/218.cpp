#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <cmath>
#include <cstdio>
using namespace std;

#define SQR(X) ((X)*(X))

typedef double flott;
typedef pair<flott,flott> point;

vector<point> pts;
int n;
list<point> U,L;


bool sup(point a, point b) {
  return (a.first > b.first)||((a.first==b.first)&&(a.second>b.second));
}


flott det(point a, point b, point c) {
  flott v1x,v1y,v2x,v2y;
  v1x = b.first - a.first;
  v1y = b.second - a.second;
  v2x = c.first - b.first;
  v2y = c.second - b.second;
  return v1x*v2y - v1y*v2x;
}

flott dist(point a, point b) {
  return sqrt(SQR(a.first-b.first)+SQR(a.second-b.second));
}

void Andrew() {
  list<point>::reverse_iterator rit;
  point a;
  sort(pts.begin(),pts.end(),sup);
  U.clear();
  L.clear();
  for (int i=0; i<n; i++) {
    while (L.size()>=2) {
      rit = L.rbegin();
      a = *rit;
      rit++;
      if (det(a,*rit,pts[i])>=0) {
	L.pop_back();
      }
      else break;
    }
    L.push_back(pts[i]);
  }
  for (int i=0; i<n; i++) {
    while (U.size()>=2) {
      rit = U.rbegin();
      a = *rit;
      rit++;
      if (det(a,*rit,pts[i])<=0) {
	U.pop_back();
      }
      else break;
    }
    U.push_back(pts[i]);
  }
  U.pop_front();
  L.pop_back();
}

int main() {
  int cpt = 1;
  bool Uvide,Lvide;
  flott x,y,per;
  list<point>::iterator it;
  list<point>::reverse_iterator rit;
  point a;

  while (cin >> n) {
    if (n==0) return 0;
    pts.clear();
    for (int i=0; i<n; i++) {
      cin >> x >> y;
      pts.push_back(point(x,y));
    }
    Andrew();

    cout << "Region #" << cpt++ << ":\n";

    Uvide = U.empty();
    Lvide = L.empty();


    if (Uvide) per = dist(L.front(),L.back());
    else if (Lvide) per = dist(U.front(),U.back());
    else per = dist(L.front(),U.front())+dist(L.back(),U.back());

    if (!Uvide) printf("(%.1f,%.1f)-",round(10*U.back().first)/10,round(10*U.back().second)/10);
    else printf("(%.1f,%.1f)-",round(10*L.back().first)/10,round(10*L.back().second)/10);

    if (!Lvide) {
      a = L.back();
      rit = L.rbegin();
      while (rit!=L.rend()) {
	per += dist(a,*rit);
	printf("(%.1f,%.1f)-",round(10*(rit->first))/10,round(10*(rit->second))/10);
	a = *rit;
	rit++;
      }
    }
    if (!Uvide) {
    it = U.begin();
    a = *it;
    while (it!=U.end()) {
      per += dist(a,*it);
      printf("(%.1f,%.1f)",round(10*it->first)/10,round(10*it->second)/10);
      a = *it;
      it++;
      if (it!=U.end()) cout << '-';
      else cout << '\n';
    }
    }
    printf("Perimeter length = %.2f\n\n",round(100*per)/100);
  }

  return 0;
}
