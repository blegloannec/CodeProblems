// ACM 10001
#include <cstdio>

#define MAX 32

int a,t;
int bruijn[4][4]; /* automate associe
		     00 01 10 11 */
char buff[MAX];

void initauto() {
  for (int i=0; i<4; i++)
    for (int j=0; j<4; j++)
      bruijn[i][j] = -1;
}

void genauto() {
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


int main() {

  initauto();  
  while (scanf("%d %d %s", &a, &t, buff)==3) { 
    genauto();
    if (accepte()) printf("REACHABLE\n");
    else printf("GARDEN OF EDEN\n");
  }

  return 0;
}
