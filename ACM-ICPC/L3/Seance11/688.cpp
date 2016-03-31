#include <iostream>
#include <list>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

typedef double flott;

struct evt {
  bool ajout;
  flott ord,deb,fin;
  evt(bool a, flott y, flott x1, flott x2) : ajout(a),ord(y),deb(x1),fin(x2) {};
};

bool sup(evt e1, evt e2) {
  return e1.ord < e2.ord;
}

vector<evt> sched;
map<flott,int> balai;

int main() {
  int nb,cas,cpt;
  flott x,y,r,x0,y0;
  vector<evt>::iterator vit;
  map<flott,int>::iterator mit;

  cas = 1;
  while (cin >> nb) {
    if (nb==0) return 0;

    sched.clear();
    while (nb-->0) {
      cin >> x >> y >> r;
      sched.push_back(evt(true,y-r,x-r,x+r));
      sched.push_back(evt(false,y+r,x-r,x+r));
    }
    sort(sched.begin(),sched.end(),sup);

    balai.clear();
    vit = sched.begin();
    y0 = vit->ord;
    r = 0;
    while (vit!=sched.end()) {
      y = vit->ord;
      while ((vit!=sched.end())&&(vit->ord==y)) {
	if (vit->ajout) {
	  mit = balai.find(vit->deb);
	  if (mit!=balai.end()) {
	    ++(mit->second);
	    if (mit->second==0) balai.erase(mit);
	  }
	  else 
	    balai.insert(pair<flott,int>(vit->deb,1));
	  mit = balai.find(vit->fin);
	  if (mit!=balai.end()) {
	    --(mit->second);
	    if (mit->second==0) balai.erase(mit);
	  }
	  else 
	    balai.insert(pair<flott,int>(vit->fin,-1));
	}
	else {
	  mit = balai.find(vit->deb);
	  if (mit!=balai.end()) {
	    --(mit->second);
	    if (mit->second==0) balai.erase(mit);
	  }
	  else 
	    balai.insert(pair<flott,int>(vit->deb,-1));
	  mit = balai.find(vit->fin);
	  if (mit!=balai.end()) {
	    ++(mit->second);
	    if (mit->second==0) balai.erase(mit);
	  }
	  else 
	    balai.insert(pair<flott,int>(vit->fin,1));
	}
	++vit;
      }
      r += x*(y-y0);
      cpt = 0;
      x = 0;
      x0 = 0;
      for (mit=balai.begin(); mit!=balai.end(); mit++) {
	if (cpt>0) x += mit->first - x0;
	x0 = mit->first;
	cpt += mit->second;
      }
      y0 = y;
    }

    printf("%d %.2f\n",cas++,round(100*r)/100);
  }

  return 0;
}
