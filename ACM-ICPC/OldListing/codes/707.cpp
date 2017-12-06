#include <iostream>
using namespace std;

#define MAX 101

int W,H,T;
bool pot[MAX][MAX][MAX];
bool sure[MAX];
bool escaped, no_sure;
int val[MAX][2];

bool read(int t, int i, int j) {
  return ((i>0)&&(i<=H)&&(j>0)&&(j<=W)&&(pot[t][i][j]));
}

bool neigh(int t, int i, int j) {
  return (read(t,i-1,j)||read(t,i,j-1)||
	  read(t,i,j)||
	  read(t,i,j+1)||read(t,i+1,j));
}

bool analyse(int t, int f) {
  if (sure[t]) return false;
  int cpt = 0;
  bool change = false;
  for (int i=1; i<=H; i++)
    for (int j=1; j<=W; j++) {
      if (pot[t][i][j]) {
	pot[t][i][j] = neigh(f,i,j);
	if (pot[t][i][j]) {
	  cpt++;
	  val[t][0] = i;
	  val[t][1] = j;
	}
	else change = true;
      }
    }
  if (cpt==0) {
    escaped = true;
    return change;
  }
  if (cpt==1) {
    sure[t] = true;
    no_sure = false;
    return true;
  }
  return change;
}

bool chrono(int tmax) {
  bool change = false;
  for (int t=2; t<=tmax; t++) 
    change = analyse(t,t-1)||change;
  return change;
}

bool reversed(int tmax) {
  bool change = false;
  for (int t=tmax; t>0; t--)
    change = analyse(t,t+1)||change; 
  return change;
}

void naif() {
  bool test = true;
  while (test) {
    test = chrono(T)&&reversed(T-1);
  }
}

int compte(int t) {
  int cpt = 0;
  for (int i=1; i<=H; i++)
    for (int j=1; j<=W; j++) 
      if (pot[t][i][j]) {
	++cpt;
	val[1][0] = i;
	val[1][1] = j;
      }
  return cpt;
}

int main() {
  int nb,tps,left,top,right,bottom,cas;
  cas = 1;

  while (cin >> W >> H >> T) {
    if ((W==0)&&(H==0)&&(T==0)) return 0;

    for (int t = 1; t<=T; t++) {
      sure[t] = false;
      for (int i=1; i<=H; i++)
	for (int j=1; j<=W; j++)
	  pot[t][i][j] = true;
    }

    cin >> nb;

    while (nb-->0) {
      cin >> tps >> left >> top >> right >> bottom;
      for (int i=top; i<=bottom; i++)
	for (int j=left; j<=right; j++)
	  pot[tps][i][j] = false;
    }

    cout << "Robbery #" << cas++ << ":\n";

    if (T==1) {
      int cpt = compte(1);
      if (cpt==0)
	cout << "The robber has escaped.\n";
      else if (cpt==1) 
	cout << "Time step 1: The robber has been at " << val[1][1] << ',' << val[1][0] << ".\n";
      else cout << "Nothing known.\n";
    }
    else {
      escaped = false;
      no_sure = true;
      
      naif();
      
      if (escaped) cout << "The robber has escaped.\n";
      else if (no_sure) cout << "Nothing known.\n";
      else {
	for (int t=1; t<=T; t++) {
	  if (sure[t]) cout << "Time step " << t << ": The robber has been at " << val[t][1] << ',' << val[t][0] << ".\n";
	}
      }
    }

    cout << '\n';

  }
  
  return 0;
}
