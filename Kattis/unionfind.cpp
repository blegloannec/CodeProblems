#include <cstdio>
#include <vector>
using namespace std;

int N;
vector<int> T;

int find(int x) {
  if (T[x]<0) return x;
  T[x] = find(T[x]);
  return T[x];
}

void merge(int x, int y) {
  T[find(y)] = find(x);
}

int main() {
  int Q;
  scanf("%d %d",&N,&Q);
  T.resize(N,-1);
  for (int q=0; q<Q; ++q) {
    char c;
    int a,b;
    scanf(" %c %d %d",&c,&a,&b);
    if (c=='?') {
      if (find(a)==find(b)) printf("yes\n");
      else printf("no\n");
    }
    else if (find(a)!=find(b)) merge(a,b);
  }
  return 0;
}
