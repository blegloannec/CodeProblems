#include <cstdio>
#include <vector>
#include <cstdlib>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

// basic greedy stuff, using square root decomposition of space...

struct cpu {
  int s,k,p;
  cpu(int s, int k, int p) : s(s), k(k), p(p) {}
  bool operator<(const cpu &B) const {
    return p<B.p || (p==B.p && s<B.s) || (p==B.p && s==B.s && k<B.k);
  }
};

struct cput {
  int s,k,p,t;
  cput(int s, int k, int p, int t) : s(s), k(k), p(p), t(t) {}
  bool operator<(const cput &B) const {
    return t<B.t || (t==B.t && s<B.s) || (t==B.t && s==B.s && k<B.k) || (t==B.t && s==B.s && k==B.k && p<B.p);
  }
};

typedef set<cpu> cpus;
typedef set<cput> cputs;

int N;
vector<int> X,Y,X0,Y0,XM,YM;
vector< vector<cpu> > S;
cpus global_free_cpu;
cputs busy_cpu;
vector< vector<cpus> > local_free_cpu;

double score(int x, int y, const cpu &C) {
  double dx = x-X[C.s], dy = y-Y[C.s];
  return sqrt(dx*dx+dy*dy) + C.p;
}

int main() {
  int Q;
  scanf("%d %d",&N,&Q);
  X.resize(N);
  Y.resize(N);
  S.resize(N);
  for (int s=0; s<N; ++s) {
    int x,y,k;
    scanf("%d %d %d",&x,&y,&k);
    X[s] = x;
    Y[s] = y;
    for (int j=0; j<k; ++j) {
      int p;
      scanf("%d",&p);
      S[s].push_back(cpu(s,j,p));
    }
  }
  int M = 4*(int)sqrt(N) + 1;
  X0 = X;
  Y0 = Y;
  sort(X0.begin(),X0.end());
  sort(Y0.begin(),Y0.begin());
  for (int i=0; i<N; i+=M) {
    XM.push_back(X0[i]);
    YM.push_back(Y0[i]);
  }
  M = XM.size()+1;
  local_free_cpu.resize(M);
  for (int i=0; i<M; ++i) local_free_cpu[i].resize(M);
  for (int s=0; s<N; ++s) {
    X0[s] = distance(XM.begin(),lower_bound(XM.begin(),XM.end(),X[s]));
    Y0[s] = distance(YM.begin(),lower_bound(YM.begin(),YM.end(),Y[s]));
    for (unsigned int i=0; i<S[s].size(); ++i) {
      local_free_cpu[X0[s]][Y0[s]].insert(S[s][i]);
      global_free_cpu.insert(S[s][i]);
    }
  }
  for (int t=0; t<Q; ++t) {
    while (!busy_cpu.empty() && busy_cpu.begin()->t<=t) {
      cput c = *(busy_cpu.begin());
      cpu c0 = cpu(c.s,c.k,c.p);
      global_free_cpu.insert(c0);
      local_free_cpu[X0[c.s]][Y0[c.s]].insert(c0);
      busy_cpu.erase(busy_cpu.begin());
    }
    printf("?\n");
    fflush(stdout);
    int x,y,bx,by;
    scanf("%d %d",&x,&y);
    bx = distance(XM.begin(),lower_bound(XM.begin(),XM.end(),x));
    by = distance(YM.begin(),lower_bound(YM.begin(),YM.end(),y));
    cpu c(0,0,0);
    double ms = 1e100;
    cpus::iterator it = local_free_cpu[bx][by].begin();
    int i = 0;
    while (i<45 && it!=local_free_cpu[bx][by].end()) {
      double s = score(x,y,*it);
      if (s<ms) {
	ms = s;
	c = *it;
      }
      ++i; ++it;
    }
    it = global_free_cpu.begin();
    i = 0;
    while (i<45 && it!=global_free_cpu.end()) {
      double s = score(x,y,*it);
      if (s<ms) {
	ms = s;
	c = *it;
      }
      ++i; ++it;
    }
    //cpu c = !local_free_cpu[bx][by].empty() ? *(local_free_cpu[bx][by].begin()) : *(global_free_cpu.begin());
    busy_cpu.insert(cput(c.s,c.k,c.p,t+c.p));
    global_free_cpu.erase(c);
    local_free_cpu[X0[c.s]][Y0[c.s]].erase(c);
    printf("! %d %d\n",c.s+1,c.k+1);
    fflush(stdout);
  }
  printf("end\n");
  fflush(stdout);
  return 0;
}
