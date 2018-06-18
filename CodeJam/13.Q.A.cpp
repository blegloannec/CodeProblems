#include <iostream>
using namespace std;

int T;
int p[4][4];
int suml[4];
int sumc[4];
int d1,d2;

char verif() {
  if (d1==3 || d1==4 || d2==3 || d2==4) return 'X';
  if (d1==-3 || d1==-4 || d2==-3 || d2==-4) return 'O';
  for (int i=0; i<4; ++i) {
    if (suml[i]==3 || suml[i]==4 || sumc[i]==3 || sumc[i]==4) return 'X';
    else if (suml[i]==-3 || suml[i]==-4 || sumc[i]==-3 || sumc[i]==-4) return 'O';
  }
  return 'D';
}

int main() {
  char c;
  bool unfinished;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    unfinished = false;
    d1 = 0;
    d2 = 0;
    for (int i=0; i<4; ++i) {
      suml[i] = 0;
      sumc[i] = 0;
    }
    for (int i=0; i<4; ++i)
      for (int j=0; j<4; ++j) {
	cin >> c;
	if (c=='X') p[i][j] = 1;
	else if (c=='O') p[i][j] = -1;
	else if (c=='.') {
	  p[i][j] = 100;
	  unfinished = true;
	}
	else p[i][j] = 0;
	sumc[i] += p[i][j];
	suml[j] += p[i][j];
	if (i==j) d1 += p[i][j];
	if (i+j==3) d2 += p[i][j];
      }
    c = verif();
    if (c!='D') cout << "Case #" << t << ": " << c << " won" << endl;
    else if (unfinished) cout << "Case #" << t << ": Game has not completed" << endl;
    else cout << "Case #" << t << ": Draw" << endl;
  }
  return 0;
}
