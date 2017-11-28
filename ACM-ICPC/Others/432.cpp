#include <cstdio>
using namespace std;

int x,y;

void line(int x1, int y1, int x2, int y2) {
  printf("(%d,%d)(%d,%d)\n",x1,y1,x2,y2);
}

void left_inv_tri(int p) {
  line(x>>p,0,x>>(p+1),y>>(p+1));
  line(x>>(p+1),y>>(p+1),(x>>p)+(x>>(p+1)),y>>(p+1));
  line((x>>p)+(x>>(p+1)),y>>(p+1),x>>p,0);
  if (p>0) line(x>>p,0,x>>(p-1),0);
}

void right_inv_tri(int p) {
  int X = x<<1;
  if (p>0) line(X-(x>>(p-1)),0,X-(x>>p),0);
  line(X-(x>>p),0,X-((x>>p)+(x>>(p+1))),y>>(p+1));
  line(X-((x>>p)+(x>>(p+1))),y>>(p+1),X-(x>>(p+1)),y>>(p+1));
  line(X-(x>>(p+1)),y>>(p+1),X-(x>>p),0);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int p,q;
    scanf("%d %d %d %d",&p,&q,&x,&y);
    line(x,y,0,0);
    if (p==0) line(0,0,x<<1,0);
    else {
      line(0,0,x>>(p-1),0);
      for (int i=p-1; i>=0; --i)
	left_inv_tri(i);
      for (int i=1; i<q; ++i)
	right_inv_tri(i);
      line((x<<1)-(x>>(q-1)),0,x<<1,0);
    }
    line(x<<1,0,x,y);
    printf("\n");
  }
  return 0;
}
