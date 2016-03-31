/* ACM 10001
   Generateur de tables deterministes */
#include <iostream>
using namespace std;

int a;
int bruijn[4][4]; /* automate associe
		     00 01 10 11 */
int det[256][16][2]; /* automate deterministe
		   table des successeurs */

void initauto() {
  for (int i=0; i<4; i++)
    for (int j=0; j<4; j++)
      bruijn[i][j] = -1;
}

void genauto(int a) {
  bruijn[0][0] = a%2; // 000
  a/=2;
  bruijn[0][1] = a%2; // 001
  a/=2;
  bruijn[1][2] = a%2; // 010
  a/=2;
  bruijn[1][3] = a%2; // 011
  a/=2;
  bruijn[2][0] = a%2; // 100
  a/=2;
  bruijn[2][1] = a%2; // 101
  a/=2;
  bruijn[3][2] = a%2; // 110
  a/=2;
  bruijn[3][3] = a%2; // 111
}

void determinise() {
  int aux, res0, res1, img0, img1, j;
  for (int i=1; i<16; i++) {
    aux = i;
    res0 = 16;
    res1 = 16;
    j = -1;
    while ((aux>0)&&(++j<4)) {
      if (aux%2==1) {
	img0 = 1;
	img1 = 1;
	for (int k=3; k>=0; k--) {
	  img0 *= 2;
	  img1 *= 2;
	  if (bruijn[j][k]==0) ++img0;
	  else if (bruijn[j][k]==1) ++img1;
	}
	res0 = res0 | img0;
	res1 = res1 | img1;
      }
      aux /= 2;
    }
    det[a][i][0] = res0%16;
    det[a][i][1] = res1%16;
  }
}


int main() {


  cout << "det[256][16][2] = {" << endl;
  initauto();  
  for (a=0; a<256; a++) {
    genauto(a);
    determinise();
    cout << '{';
    for (int i=0; i<16; i++) {
      cout << '{' << det[a][i][0] << ',' << det[a][i][1] << '}'; 
      if (i<15) cout << ',';
    }
    cout << '}';
    if (a<255) cout << ',';
    cout << endl;
  }
  cout << "};" << endl;

  return 0;
}
