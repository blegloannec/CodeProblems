// ACM 10001
#include <cstdio>

#define MAX 32

int a,t;
int bruijn[4][4]; /* automate associe
		     00 01 10 11 */
int det[256][16][2]; /* automate deterministe
		   table des successeurs */
bool done[256];
char buff[MAX];

void initauto() {
  for (int i=0; i<256; i++)
    done[i] = false;
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

/*
bool naif(int start, int curr, int pos) {
  if (pos==t) return (start==curr); // espace torique
  for (int i=0; i<4; i++)
    if ((bruijn[curr][i]==((int)buff[pos]-(int)'0')) && naif(start,i,pos+1))
      return true;
  return false;
}

bool accepte() {
  return (naif(0,0,0) || naif(1,1,0) || naif(2,2,0) || naif(3,3,0));
}
*/


bool accepte(int start) {
  int s = start;
  for (int i=0; i<t; i++) {
    s = det[a][s][(int)buff[i]-(int)'0'];
    if (s==0) return false;
  }
  return ((start & s)!=0);
}

bool accepte() {
  return (accepte(1) || accepte(2) || accepte(4) || accepte(8));
}


int main() {

  initauto();  
  while (scanf("%d %d %s", &a, &t, buff)==3) { 
    if (!done[a]) {
      genauto(a);
      determinise();
      done[a] = true;
    }
    if (accepte()) printf("REACHABLE\n");
    else printf("GARDEN OF EDEN\n");
  }

  return 0;
}
