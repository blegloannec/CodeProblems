#include <iostream>
#include <vector>
#include <queue>
#include <deque>
using namespace std;

int n;
vector<int> A;

/* one could use sparse arrays to solve each request in O(n)
   the total complexity would be O(n log n + nq)
   yet, that might be kinda overkill */

// simpler approach in O(n q log n) with one heap
int min_sliding_max_heap(int d) {
  priority_queue< pair<int,int> > Q;
  for (int i=0; i<d; ++i) Q.push(make_pair(A[i],i));
  int res = Q.top().first;
  for (int i=0; i<n-d; ++i) {
    Q.push(make_pair(A[i+d],i+d));
    while (Q.top().second<=i) Q.pop();
    res = min(res,Q.top().first);
  }
  return res;
}

// optimal O(nq) approach with one deque
int min_sliding_deque(int d) {
  deque<int> Q;
  int res = 1<<30;
  for (int i=0; i<n; ++i) {
    while (!Q.empty() && A[Q.back()]<A[i])
      Q.pop_back();
    Q.push_back(i);
    while (Q.front()<=i-d) Q.pop_front();
    // Q contains the longuest sequence of indices i-d < i1 < i2 < ... < in = i
    // such that max(A[i-d+1:i+1]) = A[i1] >= A[i2] >= ... >= A[i]
    res = min(res,A[Q.front()]);
  }
  return res;
}

int main() {
  int q;
  cin >> n >> q;
  A.resize(n);
  for (int i=0; i<n; ++i) cin >> A[i];
  for (int i=0; i<q; ++i) {
    int d;
    cin >> d;
    //cout << min_sliding_max_heap(d) << endl;
    cout << min_sliding_deque(d) << endl;
  }
  return 0;
}
