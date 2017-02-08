#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

/*
  Really poor kinda DP :-/ and poorly written too...
  runs in ~60s with -O3 but costs a lot of memory!
  Have definitely missed something about that pb!
  Should come back later with a better solution...
*/

struct triple {
  int n,m2,m3;
  triple(int n, int m2, int m3) : n(n), m2(m2), m3(m3) {}
  bool operator<(const triple &T) const {
    return n<T.n||(n==T.n && m2<T.m2)||(n==T.n && m2==T.m2 && m3<T.m3);
  }
};

enum part_t {none, one, mult};
/*
  using set instead of vector+sort for faster insertion
  and instead of unordered_set for faster comparison
  (though after a small benchmarking, it seems only ~1s
   faster overall) 
*/
typedef set<int> part_c; 

struct SpePart {
  part_t t;
  part_c *c;
  SpePart(part_t t=none, part_c *c=NULL) : t(t), c(c) {}
};

const int N = 1000000;
vector<bool> P(N,true);
map<triple,SpePart> memo;

void sieve() {
  P[0] = P[1] = false;
  for (int i=2; i<N; ++i)
    if (P[i])
      for (int k=2*i; k<N; k+=i)
	P[k] = false;
}

int expo(int a,  int n) {
  if (n==0) return 1;
  else if (n%2==0) return expo(a*a,n/2);
  else return a*expo(a*a,(n-1)/2);
}

SpePart C(int n, int max2=19, int min3=0) {
  triple h(n,max2,min3);
  auto it = memo.find(h);
  if (it!=memo.end()) return it->second;
  SpePart cs(none);
  if (n==0) {
    cs.t = one;
    cs.c = new part_c();
    return cs;
  }
  if (max2<0 || min3>12) return cs;
  SpePart c1s1 = C(n,max2-1,min3);
  if (c1s1.t==mult) {
    cs.t  = mult;
    memo[h] = cs;
    return cs;
  }
  SpePart c2s2 = C(n,max2,min3+1);
  if (c2s2.t==mult) {
    cs.t = mult;
    memo[h] = cs;
    return cs;
  }
  if (c1s1.t==one and c2s2.t==one) {
    if (*(c1s1.c)==*(c2s2.c)) {
      cs.t = one;
      cs.c = c1s1.c;
    }
    else {
      cs.t = mult;
      memo[h] = cs;
      return cs;
    }
  }
  else if (c1s1.t==one) {
    cs.t = one;
    cs.c = c1s1.c;
  }
  else if (c2s2.t==one) {
    cs.t = one;
    cs.c = c2s2.c;
  }
  int x = expo(2,max2)*expo(3,min3);
  if (x<=n) {
    SpePart c1s1 = C(n-x,max2-1,min3+1);
    if (c1s1.t==mult) {
      cs.t = mult;
      //cs.c = NULL; // who cares
      memo[h] = cs;
      return cs;
    }
    else if (c1s1.t==one) {
      part_c *s1 = new part_c();
      *s1 = *(c1s1.c); // copy
      s1->insert(x);
      if (cs.t==one && *(cs.c)!=*s1) {
	cs.t = mult;
	//cs.c = NULL; // who cares
	memo[h] = cs;
	return cs;
      }
      else {
	cs.t = one;
	cs.c = s1;
      }
    }
  }
  memo[h] = cs;
  return cs;
}
	  
int main() {
  sieve();
  int cpt = 0;
  for (int i=2; i<N; ++i)
    if (P[i] && C(i).t==one)
      cpt += i;
  cout << cpt << endl;
  return 0;
}
