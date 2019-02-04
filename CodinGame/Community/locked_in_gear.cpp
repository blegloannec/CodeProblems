#include <iostream>
#include <vector>
using namespace std;

#define SQR(X) ((X)*(X))

int N;
vector<int> X,Y,R;
vector< vector<int> > G;

/*
  The direction of u1 is defined (u1 is moving) iff:
    - u1 is in the same connected component as u0;
   &- this component is bipartite.
*/
int dfs(int u0, int u1) {
  vector<int> Q(1,u0), dir(N,0);
  dir[u0] = 1;
  while (!Q.empty()) {
    int u = Q.back(); Q.pop_back();
    for (auto iv=G[u].begin(); iv!=G[u].end(); ++iv)
      if (dir[*iv]==0) {
	dir[*iv] = -dir[u];
	Q.push_back(*iv);
      }
      else if (dir[*iv]==dir[u]) return 0;  // blocked
  }
  return dir[u1];
}

int main() {
  cin >> N;
  X.resize(N); Y.resize(N); R.resize(N);
  for (int i=0; i<N; ++i) cin >> X[i] >> Y[i] >> R[i];
  G.resize(N);
  for (int i=0; i<N; ++i)
    for (int j=i+1; j<N; ++j) {
      if (SQR(X[i]-X[j]) + SQR(Y[i]-Y[j]) == SQR(R[i]+R[j])) {
	G[i].push_back(j);
	G[j].push_back(i);
      }
    }
  int dir = dfs(0,N-1);
  if (dir==0) cout << "NOT MOVING" << endl;
  else if (dir==1) cout << "CW" << endl;
  else cout << "CCW" << endl;
  return 0;
}
