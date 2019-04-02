// Sqrt-decomposition of the y-sorted fighters in O((N+Q) sqrt N)
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <unordered_map>
using namespace std;

int N, Q, S, MaxOcc;
unordered_map<int,int> Counter;

struct fighter {
  int y, f;
  
  fighter(int y, int f=0) : y(y), f(f) {}
  
  bool operator<(const fighter &B) const {
    return y<B.y;
  }
};

vector<fighter> Fighters;

struct query {
  int y0, y1, f0, f1, b0, b1, q, res;
  
  query(int y0, int y1, int q) : y0(y0), y1(y1), q(q) {
    // fighters indices of the query (f0 included, f1 excluded)
    f0 = distance(Fighters.begin(), lower_bound(Fighters.begin(), Fighters.end(), fighter(y0)));
    f1 = distance(Fighters.begin(), upper_bound(Fighters.begin(), Fighters.end(), fighter(y1)));
    // corresponding blocks indices
    b0 = f0/S;
    b1 = f1/S;
  }
  
  bool operator<(const query &B) const {
    return b0<B.b0 || (b0==B.b0 && b1<B.b1);
  }
  
  void process() {
    /*
      Computing the result of the query in O(sqrt N)
      When this is called, Counter is assumed to already count the occurrences
      of the fighters f-values in blocks b0+1 to b1-1.
      Here we simply take into account the initial/final missing segments.
    */
    res = MaxOcc;
    if (b0==b1) {
      for (int i=f0; i<f1; ++i) res = max(res, ++Counter[Fighters[i].f]);
      for (int i=f0; i<f1; ++i) --Counter[Fighters[i].f];
    }
    else {
      for (int i=f0; i<(b0+1)*S; ++i) res = max(res, ++Counter[Fighters[i].f]);
      for (int i=b1*S; i<f1; ++i)     res = max(res, ++Counter[Fighters[i].f]);
      for (int i=f0; i<(b0+1)*S; ++i) --Counter[Fighters[i].f];
      for (int i=b1*S; i<f1; ++i)     --Counter[Fighters[i].f];
    }
  }
};

vector<query> Queries;

void process_queries() {
  sort(Queries.begin(), Queries.end());
  int q = 0;
  for (int b0=0; b0<=N/S; ++b0) {
    MaxOcc = 0;
    Counter.clear();
    for (int b1=b0; b1<=N/S; ++b1) {
      if (b1>b0+1)
	// including block b1-1 into Counter
	for (int i=(b1-1)*S; i<b1*S; ++i)
	  MaxOcc = max(MaxOcc, ++Counter[Fighters[i].f]);
      // processing queries starting in b0 and ending in b1
      while (q<Q && Queries[q].b0==b0 && Queries[q].b1==b1)
	Queries[q++].process();
    }
  }
}

int main() {
  int V_useless;
  scanf("%d %d %d", &N, &Q , &V_useless);
  S = (int)sqrt(N)+1;
  for (int i=0; i<N; ++i) {
    int x_useless, y, f;
    scanf("%d %d %d", &x_useless, &y, &f);
    Fighters.push_back(fighter(y,f));
  }
  sort(Fighters.begin(), Fighters.end());
  for (int q=0; q<Q; ++q) {
    int y0, y1, t_useless;
    scanf("%d %d %d", &y1, &y0, &t_useless);
    Queries.push_back(query(y0,y1,q));
  }
  process_queries();
  vector<int> Results(Q);
  for (int q=0; q<Q; ++q) Results[Queries[q].q] = Queries[q].res;
  for (int q=0; q<Q; ++q) printf("%d\n", Results[q]);
  return 0;
}
