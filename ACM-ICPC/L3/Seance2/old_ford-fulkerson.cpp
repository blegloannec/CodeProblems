#include <iostream>
#include <deque>
using namespace std;

class edge {
public:
  int b, e, w;
  edge(int e1, int e2, int p) : b(e1), e(e2), w(p) {};
  edge() : b(0), e(0), w(0) {};
};


int main(void) {
  int n,m;

  while (scanf("%d %d",&m,&n)==2) {
    if ((m==0)&&(n==0)) return 0;
    edge t[m];
    for (int k=0; k<m; k++) {
      int e1,e2,p;
      scanf("%d %d %d",&e1,&e2,&p);
      t[k] = edge(e1,e2,p);
    }
  } 

  return 0;

}
