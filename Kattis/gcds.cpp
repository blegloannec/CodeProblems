#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int gcd(int a, int b) {
  return b==0 ? a : gcd(b,a%b);
}

int N;
vector<int> A;

// O(N * G) DP where G <= 100 is the max of A
int consecutive_gcds() {
  unordered_set<int> All, Right;  // sizes will remain <= G
  Right.insert(0);
  for (int a : A) {
    unordered_set<int> NewRight;
    NewRight.insert(a);
    for (int g : Right) NewRight.insert(gcd(a,g));
    swap(Right, NewRight);
    for (int g : Right) All.insert(g);
  }
  return All.size();
}

int main() {
  cin >> N;
  A.resize(N);
  for (int i=0; i<N; ++i) cin >> A[i];
  cout << consecutive_gcds() << endl;
  return 0;
}
