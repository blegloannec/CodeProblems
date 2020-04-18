// It's basically about sorting fast...
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int N,C,Y;
ll A,B,X;
vector<int> S;

void generate_sequence() {
  S.resize(N);
  S[0] = A;
  A %= C;
  B %= C;
  for (int i=1; i<N; ++i)
    S[i] = (S[i-1]*B + A) % C;  
}

void radix_sort(vector<int> &A, int bsup=30, int bs=10) {
  int BS = 1<<bs;
  int Mask = BS-1;
  int N = A.size();
  for (int b=0; b<bsup; b+=bs) {
    vector< vector<int> > Bucket(BS);
    for (int i=0; i<N; ++i)
      Bucket[(A[i]>>b)&Mask].push_back(A[i]);
    int i = 0;
    for (int d=0; d<BS; ++d)
      for (auto a : Bucket[d]) A[i++] = a;
  }
}

ll compute_hash() {
  X %= Y;
  ll V = 0;
  for (auto s : S) V = (V*X + s) % Y;
  return V;
}

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> N;
    cin >> A >> B >> C;
    cin >> X >> Y;
    generate_sequence();
    int bsup = 1;
    while ((1<<bsup)<=max(S[0],(int)C)) ++bsup;
    radix_sort(S, bsup);
    cout << compute_hash() << '\n';
  }
  return 0;
}
