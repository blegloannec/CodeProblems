#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstdlib>
using namespace std;

typedef pair<int,int> pt;
typedef pair<int,pt> wpt;

int N,M;
int A[500][50][50];
vector<wpt> B[500];
int best_score = 0;
vector<pt> best_sol;

// calcule det(p2-p1, p3-p1), positif si p1, p2, p3 dans le sens direct
int det(const pt &p1, const pt &p2, const pt &p3) {
  return (p2.first-p1.first)*(p3.second-p1.second)-(p2.second-p1.second)*(p3.first-p1.first);
}

// retourne true ssi les segments [a, b] et [c, d] s'intersectent
bool inter(const pt &a, const pt &b, const pt &c, const pt &d) {
  return (det(a,b,c)*det(a,d,b)>=0) && (det(c,d,a)*det(c,b,d)>=0);
}
  
inline wpt make_wpt(int w, int i, int j) {
  return make_pair(w,make_pair(i,j));
}

void pass() {
  bool picked[N][N];
  for (int i=0; i<N; ++i)
    for (int j=0; j<N; ++j)
      picked[i][j] = false;
  int score = 0;
  vector<pt> sol;
  for (int k=0; k<M; ++k) {
    int ip = N*N, var = rand()%5;
    while (var>=0) {
      --ip;
      while (picked[B[k][ip].second.first][B[k][ip].second.second]) --ip;
      --var;
    }
    bool valid0 = false;
    while (!valid0) {
      pt p = B[k][ip].second;
      bool valid = true;
      if (k>=2 && det(sol[k-2],sol[k-1],p)==0) valid = false;
      if (valid)
	for (int l=0; l<k-2; ++l)
	  if (inter(sol[l],sol[l+1],sol[k-1],p)) {
	    valid = false;
	    break;
	  }
      if (valid) {
	score += B[k][ip].first;
	sol.push_back(p);
	picked[p.first][p.second] = true;
	valid0 = true;
      }
      else {
	--ip;
	while (ip>=0 && picked[B[k][ip].second.first][B[k][ip].second.second]) --ip;
	if (ip<0) break;
      }
    }
    if (!valid0) break;
  }
  if (score>best_score) {
    best_score = score;
    best_sol = sol;
  }
}

int main() {
  srand(42);
  scanf("%d %d",&N,&M);
  for (int k=0; k<M; ++k) {
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j) {
	scanf("%d",&A[k][i][j]);
	B[k].push_back(make_wpt(A[k][i][j],i,j));
      }
    sort(B[k].begin(),B[k].end());
  }
  for (int i=0; i<6250; ++i) pass();
  for (auto it=best_sol.begin(); it!=best_sol.end(); ++it)
    printf("%d %d\n",it->first+1,it->second+1);
  if ((int)best_sol.size()<M) printf("-1 -1\n");
  return 0;
}
