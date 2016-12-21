#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> couple;

/*
  Solution based on the longest non-decreasing subsequence
  O(n log m) where m = O(n) is the length of the solution
  runs in 30s with -O3
*/

// Commented parts allow to retrieve the solution
// yet we only need the length here
int longest_increasing_subsequence(vector<int> &X) {
  // at the beginning of iteration i
  // best[k] contains the smallest value X[j], j<i
  // ending an increasing subsequence of size k
  // we use -1 as as a "-inf" value as elements are non-negative
  vector<int> best(1,-1);
  //vector<int> pred(X.size(),-1);
  //vector<int> head(1,-1);
  for (int i=0; i<(int)X.size(); ++i) {
    // use > for increasing
    // use >= for non-decreasing
    if (X[i] >= best[best.size()-1]) {
      best.push_back(X[i]);
      //pred[i] = head[head.size()-1];
      //head.push_back(i);
    }
    else {
      // use lower_bound for increasing:
      // dicho search best[k-1] < X[i] <= best[k]
      // use upper_bound for non-decreasing:
      // dicho search best[k-1] <= X[i] < best[k]
      int k = distance(best.begin(),upper_bound(best.begin(),best.end(),X[i]));
      best[k] = X[i];
      //head[k] = i;
      //pred[i] = head[k-1];
    }
  }
  return best.size()-1;
  /* // extract solution (in reverse)
  int q = head[head.size()-1];
  vector<int> sol;
  while (q>=0) {
    sol.push_back(X[q]);
    q = pred[q];
  } */
}

int S(int n) {
  vector<couple> P;
  P.push_back(couple(1%n,1%n)); // %n for n=1 :-p
  for (int i=1; i<2*n; ++i)
    P.push_back(couple((P[i-1].first*2)%n,(P[i-1].second*3)%n));
  // on trie selon x
  sort(P.begin(),P.end());
  // on projette sur y
  vector<int> X(1,P[0].second);
  for (int i=1; i<2*n; ++i)
    if (P[i]!=P[i-1]) // on retire les points en double
      X.push_back(P[i].second);
  return longest_increasing_subsequence(X);
}

int main() {
  int s = 0;
  for (int k=1; k<=30; ++k)
    s += S(k*k*k*k*k);
  cout << s << endl;
  return 0;
}
