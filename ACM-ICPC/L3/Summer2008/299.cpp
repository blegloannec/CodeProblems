// 299

#include <cstdio>
#include <list>
using namespace std;

#define MAX 50

list<int> train;

int solve(int k) {
  if (k==0) return 0;
  int c = 0;
  list<int>::iterator it = train.begin();
  while ((*it)!=k) {
    ++it;
    ++c;
  }
  train.erase(it);
  return (k-c-1)+solve(k-1);
}

int main() {
  int n,L,t;
  scanf("%d", &n);
  while (n-->0) {
    train.clear();
    scanf("%d", &L);
    for (int i=0; i<L; i++) {
      scanf("%d", &t);
      train.push_back(t);
    }
    printf("Optimal train swapping takes %d swaps.\n", solve(L));
  }
  return 0;
}
