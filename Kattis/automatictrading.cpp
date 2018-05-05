/*
  Non trivial problem, though unfortunately the naive O(n) by request approach
  passes here (so O(n^2) overall as q ~ n).

  One possible approach would be to efficiently compute the suffix tree,
  then, for each request, compute the lowest common ancestor of the two suffix
  nodes. This costs O(n log n) overall.

  Here we simply use string hashing (same as Kattis/hashing pb) and dichotomic
  search for each request. This also costs O(n log n) overall.
*/

#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

typedef long long ent;

const ent P1 = 10007;
const ent P2 = 30011;
const ent B1 = 53;
const ent B2 = 59;

int N;
char S[100001];
vector<ent> H1,H2,Bpow1,Bpow2;

void init_hash() {
  N = strlen(S);
  H1.resize(N+1,0);
  H2.resize(N+1,0);
  Bpow1.resize(N+1,1);
  Bpow2.resize(N+1,1);
  for (int i=0; i<N; ++i) {
    ent c = S[i]>='a' ? S[i]-'a'+1 : S[i]-'A'+27;
    H1[i+1] = (((B1*H1[i])%P1) + c) % P1;
    H2[i+1] = (((B2*H2[i])%P2) + c) % P2;
    Bpow1[i+1] = (Bpow1[i]*B1) % P1;
    Bpow2[i+1] = (Bpow2[i]*B2) % P2;
  }
}

int get_hash(int L, int R) {
  int h1 = (((H1[R] - ((H1[L]*Bpow1[R-L])%P1)) % P1) + P1) % P1;
  int h2 = (((H2[R] - ((H2[L]*Bpow2[R-L])%P2)) % P2) + P2) % P2;
  return h1 | (h2<<16);
}

int dicho(int i, int j) {
  int l = 0, r = N-max(i,j);
  while (l<r) {
    int k = (l+r+1)/2;
    if (get_hash(i,i+k)==get_hash(j,j+k)) l = k;
    else r = k-1;
  }
  return l;
}

int main() {
  scanf("%s",S);
  init_hash();
  int Q;
  scanf("%d",&Q);
  for (int q=0; q<Q; ++q) {
    int i,j;
    scanf("%d %d",&i,&j);
    printf("%d\n",dicho(i,j));
  }
  return 0;
}
