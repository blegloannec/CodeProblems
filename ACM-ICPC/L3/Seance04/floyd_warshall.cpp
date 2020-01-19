// Arbitrage

#include <iostream>
#include <math.h>
#include <list>
using namespace std;

#define MAX 22

int n;
float t[MAX][MAX];
float w[MAX][MAX];
int pi[MAX][MAX];
list<int> vert,vertmin;


/* // Version sans memorisation du chemin
void FloydWarshall() {
  for (int k=0; k<n; k++)
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++)
	w[i][j] = min(w[i][j],w[i][k]+w[k][j]);
}
*/

void FloydWarshall() {
  int c;
  for (int i=0; i<n; i++)
    for (int j=0; j<n; j++) 
      pi[i][j] = i;
  for (int k=0; k<n; k++)
    for (int i=0; i<n; i++) {
      for (int j=0; j<n; j++) {
	c = w[i][k] + w[k][j];
	if (w[i][j] > c) {
	  w[i][j] = c;
	  pi[i][j] = pi[k][j];
	}
      }
    }
}

void Chemin(int r) {
  vert.clear();
  int cc = pi[r][r];
  while (cc != r) {
    vert.push_front(cc+1);
    cc = pi[r][cc];
  }
}  
  

int main() {
  float f;

  while (cin >> n) {
    for (int i=0; i<n; i++)
      for (int j=0; j<n; j++) {
	if (i==j) t[i][j] = 0;
	else { 
	  cin >> f;
	  t[i][j] = -log(f);
	}
	w[i][j] = t[i][j];
      }
    
    FloydWarshall();
    
    vertmin.clear();
    
    for (int i=0; i<n; i++) {
      if (w[i][i]<0) {
	Chemin(i);
	if (vert.size() < vertmin.size()) vertmin = vert;
      }
    }
    
    if (vertmin.empty()) cout << "no arbitrage sequence exists\n";
    else {
      for (list<int>::iterator it=vertmin.begin(); it!=vertmin.end(); it++) 
	cout << *it << ' ';
      cout << endl;
    }

  }

  return 0;
}
