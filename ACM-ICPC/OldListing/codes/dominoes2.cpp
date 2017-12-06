#include <stdio.h>
//using namespace std;

#define MAX 25

int f(int n);
int p[MAX];

int fh(int n);
int ph[MAX];

int fb(int n);
int pb[MAX];

int fm(int n);
int pm[MAX];


int f(int n) {
  if (n==0) return 0;
  else if (n==1) return 1;
  else if (n==2) return 5;
  else {
    int m = p[n];
    if (m>=0) return m;
    else {
      m = f(n-2)+f(n-1)+fb(n-1)+2*fh(n-1);
      p[n] = m;
      return m;
    }      
  }
}

int fh(int n) {
  if (n==0) return 0;
  else if (n==1) return 1;
  else {
    int m = ph[n];
    if (m>=0) return m;
    else {
      m = f(n-1)+fh(n-1);
      ph[n] = m;
      return m;
    }      
  }
}

int fb(int n) {
  if (n==0) return 0;
  else if (n==1) return 1;
  else {
    int m = pb[n];
    if (m>=0) return m;
    else {
      m = f(n-1)+fm(n-1);
      pb[n] = m;
      return m;
    }      
  }
}

int fm(int n) {
  if (n==0) return 0;
  else if (n==1) return 0;
  else {
    int m = pm[n];
    if (m>=0) return m;
    else {
      m = fb(n-1);
      pm[n] = m;
      return m;
    }      
  }
} 

int main(void) {
  
  for (int i=0; i<MAX; i++) {
    p[i]=-1;
    pb[i]=-1;
    pm[i]=-1;
    ph[i]=-1;
  }

  int N,c;
  scanf("%d",&N);
  c = 0;
  
  while (c++ < N) {
    int n;
    scanf("%d",&n);
    printf("%d %d\n",c,f(n));
  }

  return 0;
}
