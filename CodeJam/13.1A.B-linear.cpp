#include <iostream>
#include <stack>
using namespace std;

typedef long long ent;

#define NMAX 10001

int E,R,N;
int v[NMAX];
int next_sup[NMAX];
stack<int> P;

// Glouton en O(NMAX)

/* On utilise next_sup[i] = min{ j>i | v[j]>v[i] } (parfois appelé Stock Span Problem)
   Calculé en O(n) en parcourant v[] de droite à gauche et
   en stockant dans une pile la séquence extraite des valeurs croissantes
   de la position courante à la fin du tableau (i.e. le "profil" des valeurs
   "visibles" depuis la position i, où ne figurent pas les positions cachées
   par des valeurs plus grandes les précédant).
*/
   
int main() {
  int T,ns;
  ent gain,Ecurr,Emax_ns,Ecurr_min;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    cin >> E >> R >> N;
    R = min(E,R);
    for (int i=0; i<N; ++i) cin >> v[i];
    while (!P.empty()) P.pop();
    for (int i=N-1; i>=0; --i) {
      while (!P.empty() && v[P.top()]<=v[i]) P.pop();
      if (!P.empty()) next_sup[i] = P.top();
      else next_sup[i] = 0; // pas de next sup
      P.push(i);
    }
    gain = 0;
    Ecurr = E;
    for (int i=0; i<N; ++i) {
      Ecurr = min((ent)E,Ecurr+(ent)R);
      ns = next_sup[i];
      if (ns>0) {
	Emax_ns = (ent)Ecurr+(ent)(ns-i)*(ent)R;
	if (Emax_ns>E) { // il va y avoir des pertes
	  Ecurr_min = max((ent)0,(ent)E-(ent)(ns-i)*(ent)R);
	  gain += (Ecurr-Ecurr_min)*(ent)v[i];
	  Ecurr = Ecurr_min;
	}
	// sinon on économise
      }
      else { // pas de next sup, on consomme tout sur place
	gain += (ent)Ecurr*(ent)v[i];
	Ecurr = 0;
      }
    }
    cout << "Case #" << t << ": " << gain << endl;
  }
  return 0;
}
