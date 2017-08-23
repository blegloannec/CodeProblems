#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

/*
  Par inversion de l'une et composition, on ramene tout a la distance a l'id.
  On pre-calcule les distances a l'id des 10! permutations par BFS.
  Une permutation sera representee par un entier en base 10 de 10 chiffres.
  ~15s avec -O3 pour le calcul complet (la distance max est 9)
*/

typedef long long ll;
const int B = 10;
const int S = 10;
vector<ll> Bpow(S,1);

inline ll digit(ll p, int i) {
  return (p/Bpow[i])%B;
}

vector<ll> succ(ll p) {  // O(S^2)
  vector<ll> res;
  for (int i=0; i<S; ++i) {
    // intervalles pairs centres en (i,i+1)
    ll q = p;
    for (int k=0; 0<=i-k && i+1+k<S; ++k) {
      ll a = digit(q,i-k);
      ll b = digit(q,i+1+k);
      q += (b-a)*Bpow[i-k] + (a-b)*Bpow[i+1+k];
      res.push_back(q);
    }
    // intervalles impair centres en i
    q = p;
    for (int k=1; 0<=i-k && i+k<S; ++k) {
      ll a = digit(q,i-k);
      ll b = digit(q,i+k);
      q += (b-a)*Bpow[i-k] + (a-b)*Bpow[i+k];
      res.push_back(q);
    }
  }
  return res;
}

unordered_map<ll,int> dist;

void bfs(ll u=123456789LL) {
  queue<ll> Q;
  dist[u] = 0;
  Q.push(u);
  while (!Q.empty()) {
    u = Q.front();
    Q.pop();
    vector<ll> neigh = succ(u);
    for (vector<ll>::iterator iv=neigh.begin(); iv!=neigh.end(); ++iv)
      if (dist.find(*iv)==dist.end()) {
	dist[*iv] = dist[u]+1;
	Q.push(*iv);
      }
  }
}

vector<int> compose(vector<int> &X, vector<int> &Y) {
  vector<int> XY(S);
  for (int i=0; i<S; ++i) XY[i] = X[Y[i]];
  return XY;
}

vector<int> inverse(vector<int> &X) {
  vector<int> Xinv(S);
  for (int i=0; i<S; ++i) Xinv[X[i]] = i;
  return Xinv;
}

int main() {
  for (int i=1; i<S; ++i) Bpow[i] = Bpow[i-1]*B;
  bfs();
  const int nbl = 5;
  for (int i=0; i<nbl; ++i) {
    vector<int> X(S), Y(S);
    int a;
    for (int j=0; j<10; ++j) {
      cin >> a;
      X[j] = a-1;
    }
    for (int j=0; j<10; ++j) {
      cin >> a;
      Y[j] = a-1;
    }
    vector<int> Xinv = inverse(X);
    vector<int> XinvY = compose(Xinv,Y);
    ll C = 0;
    for (int j=0; j<S; ++j) C = B*C + (ll)XinvY[j];
    cout << dist[C];
    if (i<nbl-1) cout << ' ';
    else cout << endl;
  }
  return 0;
}
