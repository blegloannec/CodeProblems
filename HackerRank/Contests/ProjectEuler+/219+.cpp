#include <iostream>
#include <map>
using namespace std;
using ll = long long;

const ll P = 1000000007;

/*
  Algo glouton : pour construire un code optimal d'ordre N+1 a partir d'un
  code optimal d'ordre N, prendre la feuille de plus petit poids x et creer
  2 fils a cet endroit de poids x+a et x+b.
  Optimisation : maintenir le compte de feuilles de chaque poids pour
  accelerer le processus.
*/

int main() {
  int Q;
  cin >> Q;
  for (int q=0; q<Q; ++q) {
    ll n, a, b, cost = 0;
    cin >> n >> a >> b;
    map<ll,ll> Count;
    Count[0] = 1;
    --n;
    while (n>0) {
      auto it = Count.begin();
      ll x = it->first, c = it->second;
      if (c>n) {
	c = n;
	Count[x] -= c;
      }
      else Count.erase(it);
      n -= c;
      Count[x+a] += c;
      Count[x+b] += c;
      cost = (cost + c*(x+a+b)) % P;
    }
    cout << cost << endl;
  }
  return 0;
}
