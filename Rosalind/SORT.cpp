#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef pair< ll, pair<int,int> > succ_pos;
const int B = 10;
const int S = 10;
vector<ll> Bpow(S,1);

inline ll digit(ll p, int i) {
  return (p/Bpow[i])%B;
}

vector<succ_pos> succ(ll p) {  // O(S^2)
  vector<succ_pos> res;
  for (int i=0; i<S; ++i) {
    // intervalles pairs centres en (i,i+1)
    ll q = p;
    for (int k=0; 0<=i-k && i+1+k<S; ++k) {
      ll a = digit(q,i-k);
      ll b = digit(q,i+1+k);
      q += (b-a)*Bpow[i-k] + (a-b)*Bpow[i+1+k];
      res.push_back(make_pair(q,make_pair(i-k,i+1+k)));
    }
    // intervalles impair centres en i
    q = p;
    for (int k=1; 0<=i-k && i+k<S; ++k) {
      ll a = digit(q,i-k);
      ll b = digit(q,i+k);
      q += (b-a)*Bpow[i-k] + (a-b)*Bpow[i+k];
      res.push_back(make_pair(q,make_pair(i-k,i+k)));
    }
  }
  return res;
}

unordered_map<ll,int> dist;
unordered_map<ll,succ_pos> pred;

void bfs(ll u, ll dst) {
  queue<ll> Q;
  dist[u] = 0;
  Q.push(u);
  while (!Q.empty()) {
    u = Q.front();
    Q.pop();
    vector<succ_pos> neigh = succ(u);
    for (vector<succ_pos>::iterator iv=neigh.begin(); iv!=neigh.end(); ++iv) {
      ll v = iv->first;
      if (dist.find(v)==dist.end()) {
	dist[v] = dist[u]+1;
	pred[v] = make_pair(u,iv->second);
	if (v==dst) return;
	Q.push(v);
      }
    }
  }
}

// construction d'un chemin optimal par remontee
void print_path(ll X, ll Y) {
  if (Y!=X) {
    succ_pos PY = pred[Y];
    print_path(X,PY.first);
    // attention, on a renverse les entrees, donc on re-inverse ici
    cout << S-PY.second.second << ' ' << S-PY.second.first << endl;
  }
}

int main() {
  for (int i=1; i<S; ++i) Bpow[i] = Bpow[i-1]*B;
  ll X = 0, Y = 0;
  int a;
  for (int j=0; j<10; ++j) {
    cin >> a;
    X = B*X + a-1;
  }
  for (int j=0; j<10; ++j) {
    cin >> a;
    Y = B*Y + a-1;
  }
  bfs(X,Y);
  cout << dist[Y] << endl;
  print_path(X,Y);
  return 0;
}
