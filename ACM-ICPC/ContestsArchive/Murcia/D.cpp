#include<iostream>
#include<cmath>
using namespace std;

#define MAX 50000

int tleft[MAX];
int tright[MAX];
int weight[MAX];

int main() {
  int cas,W,H,h,res,curri,p,pos;
  char c;
  bool side;
  cin >> cas;

  while (cas-->0) {
    cin >> W >> H;
    curri = 0;
    weight[0] = 1;
    for (int i=0; i<H; ++i) {
      tleft[curri] = -1;
      for (int j=0; j<W; ++j) {
	cin >> c;
	int toto = c-'0';
	if (toto%2 == 0) {
	  if (tleft[curri]<0) 
	    tleft[curri] = j;
	  tright[curri] = j;
	}
      }
      if (curri==0) {
	if (tleft[curri] < 0) 
	  tleft[curri] = tright[curri] = 0;
	++curri;
	weight[curri] = 1;   
	tleft[curri] = -1;
      }
      else {
	if (tleft[curri] >= 0) {
	  ++curri;
	  weight[curri] = 1;   
	  tleft[curri] = -1;
	}
	else 
	  ++weight[curri];
      }
    }
    
    h = 0;
    res = 0;
    pos = 0;
    side = true; // pour left
    tleft[0] = 0;
    while (h < curri-1) {
      //      cout << h << endl;
      side = (pos <= tleft[h]);
      if (side) { // on va vers la droite
	if (tright[h] <= tleft[h+1])
	  p = tleft[h+1];
	else
	  p = max(tright[h],tright[h+1]);
	if (p>pos) 
	  res += p - pos;
	pos = p;
      }
      else {
	if (tleft[h] >= tright[h+1])
	  p = tright[h+1];
	else 
	  p = min(tleft[h],tleft[h+1]);
	if (p<pos)
	  res += pos - p;
	pos = p;
      }
      res += weight[h+1];
      //      cout << '\t' << pos << ' ' << res << endl;
      ++h;
    }
    // cas h=curri-1;
    //    cout << pos << endl;
    //    cout << tleft[h] << endl;
    side = (pos <= tleft[h]);
    if (side) { // on va vers la droite
      p = tright[h];
      if (p>pos) 
	res += p - pos;
    }
    else {
      p = tleft[h];
      if (p<pos)
	res += pos - p;
    }
    cout << res << '\n';
  }

  return 0;
}
