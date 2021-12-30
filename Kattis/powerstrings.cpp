#include <iostream>
#include <vector>
#include <string>
using namespace std;

void prefs(const string &B, vector<int> &P) {
  P.resize(B.size()+1);
  P[0] = -1;
  int k = -1;
  for (int i=1; i<=(int)B.size(); ++i) {
    while (k>=0 && B[i-1]!=B[k]) k = P[k];
    ++k;
    P[i] = k;
  }
}

int kmp(const string &A, const string &B, int i0=0) {
  vector<int> P;
  prefs(B,P);
  int k = 0;
  for (int i=i0; i<(int)A.size(); ++i) {
    while (k>=0 && A[i]!=B[k]) k = P[k];
    ++k;
    if (k==(int)B.size())
      return i-(int)B.size()+1;
  }
  return -1;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string S;  
  vector<int> P;  
  while (true) {
    cin >> S;
    if (S==".") break;
    
    /* 
      Method 0: the (S+S).find(S,1) trick
      Unfortunately using STL string find is too slow!..
      (theoretically it should be linear, but...)
      We have to use out own KMP.
    */
    //int p = kmp(S+S, S, 1);
    
    /*
      Method 1: using "borders" (twice as fast in practice)
      We do not really need KMP, the prefix array is enough.
      Its last cell gives the size of the longest strict prefix
      that is also a suffix of S, hence it must be:
        length of S - shortest period
    */
    prefs(S,P);
    int p = S.size()-P.back();
    
    // output
    cout << S.size()/p << endl;
  }
  return 0;
}
