#include <iostream>
using namespace std;

#define MAX 1001
#define W 510

string t[2][W];
int p[W][W];
int nb[2];
char buff[MAX];
string curr;


void add(int i) {
  if (curr=="") return;
  t[i][nb[i]] = curr;
  nb[i] += 1;
  curr = "";
}

void analyse(int i) {
  int c = 0;
  nb[i] = 0;
  curr = "";
  while (buff[c]!=0 && buff[c]!='\n') {
    if ((buff[c]>='a' && buff[c]<='z') ||
	(buff[c]>='A' && buff[c]<='Z') ||  
	(buff[c]>='0' && buff[c]<='9'))
      curr = curr + buff[c];
    else add(i);
    ++c;
  }    
  add(i);
}

int plssc(int i, int j) {
  if (i<0 || j<0) return 0;
  if (p[i][j]>=0) return p[i][j];
  int res = 0;
  if (t[0][i]==t[1][j]) {
    res = 1+plssc(i-1,j-1);
  }
  res = max(res,plssc(i-1,j));
  res = max(res,plssc(i,j-1));
  p[i][j] = res;
  return res;
}

int main() {
  int cas = 1;
  bool blank;
  while (!cin.getline(buff,MAX).eof()) {
    blank = (buff[0] == 0);
    analyse(0);
    cin.getline(buff,MAX);
    blank = blank || (buff[0] == 0);
    analyse(1);

    if (cas<10) cout << ' ';
    if (blank) cout << cas << ". Blank!\n";
    else {
      for (int i=0; i<nb[0]; ++i)
	for (int j=0; j<nb[1]; ++j)
	  p[i][j] = -1;
      int res = plssc(nb[0]-1,nb[1]-1);
      cout << cas << ". Length of longest match: " << res << '\n';
    }
    ++cas;
  }
  return 0;
}
