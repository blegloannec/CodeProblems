#include <iostream>
#include <stack>
#include <cassert>
using namespace std;

template <typename T>
struct queue {
  stack<T> in,out;

  queue() {}

  bool empty() {
    return (in.empty() && out.empty());
  }
  
  void push(T x) {
    in.push(x);
  }

  void transfer() {
    assert(out.empty());
    while (!in.empty()) {
      out.push(in.top());
      in.pop();
    }
  }
  
  void pop() {
    if (out.empty()) transfer();
    assert(!out.empty());
    out.pop();
  }

  T front() {
    if (out.empty()) transfer();
    assert(!out.empty());
    return out.top();
  }
};

int main() {
  int q;
  cin >> q;
  queue<int> Q;
  for (int i=0; i<q; ++i) {
    int t;
    cin >> t;
    if (t==1) {
      int x;
      cin >> x;
      Q.push(x);
    }
    else if (t==2) Q.pop();
    else cout << Q.front() << endl;
  }
  return 0;
}
