#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

/* Fenwick Trees */
typedef long long ent;

struct Fenwick {
  vector<ent> FT;

  void add(int i, ent v);
  ent prefix_sum(int i) const;

  // variante range
  void range_add(int a, int b, ent v);

  ent operator[](int i) const;

  Fenwick(int n=0) {
    FT.resize(n+1,0);
  }

  void resize(int n) {
    FT.resize(n+1,0);
  }
};

void Fenwick::add(int i, ent v=1) {
  //assert(i>0);
  while (i<(int)FT.size()) {
    FT[i] += v;
    i += i&-i;
  }
}

ent Fenwick::prefix_sum(int i) const { // prefix sum
  ent s = 0;
  while (i>0) {
    s += FT[i];
    i -= i&-i;
  }
  return s;
}

void Fenwick::range_add(int a, int b, ent v=1) {
  add(a,v);
  add(b+1,-v);
}

// variante range
ent Fenwick::operator[](int i) const {
  return prefix_sum(i);
}


int N;
Fenwick F;
vector<int> A,Next,BigNext,BigCount;

void maj(int L) {
  deque<int> S;
  for (int i=min(L+101,N); i>=max(1,L-101); --i) {
    while (!S.empty() && F[S.back()]<=F[i]) S.pop_back();
    if (i<=L) {
      if (!S.empty() && S.back()-i<=100) Next[i] = S.back();
      else Next[i] = i;
    }
    S.push_back(i);
    while (S.front()-i>100) S.pop_front();
    if (i<=L) {
      BigNext[i] = S.front();
      BigCount[i] = S.size()-1;
    }
  }
}

int main() {
  int Q,a,t,i,k,L,R,X;
  scanf("%d %d",&N,&Q);
  F.resize(N);
  A.resize(N+1);
  for (int i=1; i<=N; ++i) {
    scanf("%d",&a);
    F.range_add(i,i,a);
    A[i] = a;
  }
  Next.resize(N+1);
  BigNext.resize(N+1);
  BigCount.resize(N+1);
  deque<int> S;
  for (int i=N; i>=1; --i) {
    while (!S.empty() && A[S.back()]<=A[i]) S.pop_back();
    if (!S.empty() && S.back()-i<=100) Next[i] = S.back();
    else Next[i] = i;
    S.push_back(i);
    while (S.front()-i>100) S.pop_front();
    BigNext[i] = S.front();
    BigCount[i] = S.size()-1;
  }
  for (int q=0; q<Q; ++q) {
    scanf("%d",&t);
    if (t==1) {
      scanf("%d %d",&i,&k);
      while (k>0 && Next[i]!=i) {
	if (k>=BigCount[i]) {
	  k -= BigCount[i];
	  i = BigNext[i];
	}
	else {
	  i = Next[i];
	  --k;
	}
      }
      printf("%d\n",i);
    }
    else {
      scanf("%d %d %d",&L,&R,&X);
      F.range_add(L,R,X);
      maj(L);
      maj(R);
    }
  }
  return 0;
}
