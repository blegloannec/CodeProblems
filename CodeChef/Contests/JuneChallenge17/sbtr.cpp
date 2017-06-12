#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
using namespace std;

/*
  Derniere version soumise du code, mais pas celle donnant le meilleur score.
  L'approche gloutonne ne permet pas d'ameliorer le score, le meilleur score
  est obtenu sans utiliser greedy_bfs, avec 1150 runs initiales du dfs
  (+ les 100 rerun sur les meilleurs + 100 runs sur les plus gros).
*/

int N;
vector< vector<int> > G;
vector<int> C;
vector<bool> seen,taken;

bool comp(int i, int j) {
  return C[i]<C[j];
}

void shuffle(vector<int> &A) {
  for (int i=A.size()-1; i>0; --i)
    swap(A[i],A[rand()%i]);
}

int dfs0(int u, int u0=-1) {
  if (seen[u]) return 0;
  seen[u] = true;
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0 && taken[*iv]) return 0;
  taken[u] = true;
  int res = C[u];
  shuffle(G[u]);
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    res += dfs0(*iv,u);
  return res;
}

int dfs(int u) {
  fill(seen.begin(),seen.end(),false);
  fill(taken.begin(),taken.end(),false);
  return dfs0(u);
}

int greedy_bfs(int u0) {
  int res = 0;
  priority_queue< pair<float,int> > Q;
  fill(seen.begin(),seen.end(),false);
  fill(taken.begin(),taken.end(),false);
  vector<bool> queued(N,false);
  Q.push(make_pair((float)C[u0]/(float)G[u0].size(),u0));
  queued[u0] = true;
  while (!Q.empty()) {
    int u = Q.top().second;
    Q.pop();
    seen[u] = true;
    bool take = true;
    for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
      if (*iv!=u0 && taken[*iv]) {
	take = false;
	break;
      }
    if (take) {
      taken[u] = true;
      res += C[u];
      for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
	if (!queued[*iv]) {
	  Q.push(make_pair((float)C[*iv]/(float)G[*iv].size(),*iv));
	  queued[*iv] = true;
	}
    }
  }
  return res;
}

int main() {
  srand(43);
  int M,u,v;
  scanf("%d %d",&N,&M);
  C.resize(N);
  for (int i=0; i<N; ++i) scanf("%d",&C[i]);
  G.resize(N);
  for (int i=0; i<M; ++i) {
    scanf("%d %d",&u,&v); --u; --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  seen.resize(N);
  taken.resize(N);
  int best_score = -1;
  vector<bool> best_taken;
  vector< pair<int,int> > scores;
  // max acceptable 1350
  for (int i=0; i<1100; ++i) {
    u = rand()%N;
    int s = dfs(u);
    if (s>best_score) {
      best_score = s;
      best_taken = taken;
    }
    scores.push_back(make_pair(s,u));
  }
  for (int i=0; i<600; ++i) {
    u = rand()%N;
    int s = greedy_bfs(u);
    if (s>best_score) {
      best_score = s;
      best_taken = taken;
    }
  }
  // on en relance 10 sur chacun des 10 meilleurs
  sort(scores.begin(),scores.end());
  for (int i=0; i<10; ++i) {
    u = scores[scores.size()-1-i].second;
    int s = greedy_bfs(u);
    if (s>best_score) {
      best_score = s;
      best_taken = taken;
    }
    for (int j=0; j<10; ++j) {
      int s = dfs(u);
      if (s>best_score) {
	best_score = s;
	best_taken = taken;
      }
    }
  }
  // on lance sur les 10 plus gros sommets
  vector<int> S(N);
  for (int i=0; i<N; ++i) S[i] = i;
  sort(S.begin(),S.end(),comp);
  for (int i=0; i<10 && i<(int)S.size(); ++i) {
    u = S[S.size()-1-i];
    int s = greedy_bfs(u);
    if (s>best_score) {
      best_score = s;
      best_taken = taken;
    }
    for (int j=0; j<10; ++j) {
      int s = dfs(u);
      if (s>best_score) {
	best_score = s;
	best_taken = taken;
      }
    }
  }
  // output
  vector<int> res;
  for (int i=0; i<N; ++i)
    if (!best_taken[i]) res.push_back(i+1);
  printf("%ld\n",res.size());
  if (res.size()>0) {
    printf("%d",res[0]);
    for (unsigned int i=1; i<res.size(); ++i)
      printf(" %d",res[i]);
  }
  printf("\n");
  return 0;
}
