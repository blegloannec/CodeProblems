// Prog dyn pour "Always on the run"

#include <iostream>
using namespace std;

#define MAXDAY 1002
#define MAXCITY 12
#define MAXPERIOD 32
#define INTMAX 5000000


int n,k;
int mem[MAXCITY][MAXDAY];
int flight[MAXCITY][MAXCITY][MAXPERIOD];
int period[MAXCITY][MAXCITY];

int calcul(int i, int j) {
  if (j<=0) {
    if (i==0) return 0;
    else return INTMAX;
  }
  int m = mem[i][j];
  if (m>=0) return m;
  int mini = INTMAX;
  int c=0;
  while (c<n) {
    if (c!=i) 
      mini = min(mini,calcul(c,j-1)+flight[c][i][(j-1) % (period[c][i])]);
    ++c;
  }
  mem[i][j] = mini;
  return mini;
}


int main() {
  int i,j,q,p,f,res;
  int s = 1;

  while (cin >> n >> k) {
    if ((n==0)&&(k==0)) return 0;
    for (i=0; i<n; i++)
      for (j=0; j<=k; j++)
	mem[i][j] = -1;
    for (i=0; i<n; i++) {
      j = 0;
      while (j<n) {
	if (j!=i) {
	  cin >> p;
	  period[i][j] = p;
	  for (q=0; q<p; q++) {
	    cin >> f;
	    if (f>0) flight[i][j][q] = f;
	    else flight[i][j][q] = INTMAX;
	  }
	}
	++j;
      }      
    }    
    
    cout << "Scenario #" << s << '\n';
    res = calcul(n-1,k);
    if (res>=INTMAX) cout << "No flight possible.\n\n";
    else cout << "The best flight costs " << res << ".\n\n";
    
    ++s;

  }

  return 0;
}
