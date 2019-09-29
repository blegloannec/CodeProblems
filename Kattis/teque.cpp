#include <cstdio>
#include <deque>
using namespace std;

typedef int elem;

struct Teque {
  deque<elem> left, right;

  void push_back(elem x) {
    right.push_back(x);
  }

  void push_front(elem x) {
    left.push_front(x);
  }

  void push_middle(elem x) {
    while (left.size() < right.size()) {
      left.push_back(right.front());
      right.pop_front();
    }
    while (left.size()-right.size()>1) {
      right.push_front(left.back());
      left.pop_back();
    }
    right.push_front(x);
  }

  elem get(unsigned int i) {
    return i<left.size() ? left[i] : right[i-left.size()];
  }
};

int main() {
  Teque T;
  int N;
  scanf("%d", &N);
  for (int i=0; i<N; ++i) {
    char op[15]; int x;
    scanf("%s %d", op, &x);
    if (op[0]=='g') printf("%d\n", T.get(x));
    else if (op[5]=='b') T.push_back(x);
    else if (op[5]=='f') T.push_front(x);
    else T.push_middle(x);
  }
  return 0;
}
