#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

typedef long long ent;

/*
  N = 17526*10**9
  
  http://oeis.org/A008443
  La reference http://www.personal.psu.edu/jxs23/p7.pdf
  Hirschhorn-Sellers, On Representations Of A Number As A Sum Of Three Triangles
  donne (p2) la formule G(3^(2l+1)n + (19*3^(2l)-3)/8) = (2*3^l-1) * G(3n+2)
  qui s'applique ici pour l = 4 et n = 890413046 :
  G(N) = G(3^9*890413046 + (19*3^8-3)/8) = 161 * G(2671239140)
*/

const ent N = 2671239140;

int main() {
  vector<ent> T;
  unordered_set<ent> X;
  ent n = 0, t = 0;
  while (t<=N) {
    T.push_back(t);
    X.insert(N-t);
    ++n;
    t = n*(n+1)/2;
  }
  
  ent cpt = 0;
  for (unsigned int i=0; i<T.size() && 2*T[i]<=N; ++i) {
    if (X.find(2*T[i])!=X.end()) ++cpt;
    for (unsigned int j=i+1; j<T.size() && T[i]+T[j]<=N; ++j)
      if (X.find(T[i]+T[j])!=X.end()) cpt += 2;
  }
  cout << 161*cpt << endl;
  
  return 0;
}
