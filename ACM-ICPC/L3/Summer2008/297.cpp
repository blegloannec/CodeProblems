// ACM 297

#include <cstdio>

#define MAX 32

bool A[MAX][MAX];
bool B[MAX][MAX];
char buff[3000];
int k;

void lire(bool T[MAX][MAX], int x, int y, int c) {
  if (buff[k]=='f') {
    for(int i=x; i<x+c; i++) 
      for (int j=y; j<y+c; j++)
	T[i][j] = true;
    ++k;
  }
  else if (buff[k]=='e') {
    for(int i=x; i<x+c; i++) 
      for (int j=y; j<y+c; j++)
	T[i][j] = false;
    ++k;
  }
  else {
    ++k;
    lire(T,x,y+c/2,c/2);
    lire(T,x,y,c/2);
    lire(T,x+c/2,y,c/2);
    lire(T,x+c/2,y+c/2,c/2);
  }
}

int compte() {
  int res = 0;
  for(int i=0; i<MAX; i++) 
    for (int j=0; j<MAX; j++) 
      if (A[i][j] || B[i][j]) ++res;
  return res;
}

int main() {
  int n;
  scanf("%d", &n);
  while (n-->0) {
    scanf("%s", buff);
    k = 0;
    lire(A,0,0,MAX);
    scanf("%s", buff);
    k = 0;
    lire(B,0,0,MAX);
    printf("There are %d black pixels.\n", compte());
  }
  return 0;
}

