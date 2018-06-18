#include <iostream>
using namespace std;

#define NMAX 1000

int T,N;
int a[NMAX];
int b[NMAX];
int progress[NMAX];

int main() {
  int s,s0,l,imaxb;
  cin >> T;
  for (int c=1; c<=T; ++c) {
    cin >> N;
    for (int i=0; i<N; ++i) {
      progress[i] = 0;
      cin >> a[i] >> b[i];
    }
    s0 = -1;
    s = 0;
    l = 0;
    // Glouton sur le prochain niveau a faire
    while (s>s0) {
      s0 = s;
      for (int i=0; i<N; ++i) {
	// si on peut faire un **, on en prend un
	if (progress[i]<2 && b[i]<=s) {
	  s += 2-progress[i];
	  progress[i] = 2;
	  ++l;
	}
      }
      if (s==s0) {
	/* sinon il faut choisir un *
	   on prend celui pour lequel le **
	   est le plus dur
	   Exemple (en 3 coups) :
	   2
	   0 1
	   0 3
	*/
	imaxb = -1;
	for (int i=0; i<N; ++i) {
	  if (progress[i]==0 && a[i]<=s && (imaxb<0 || b[i]>b[imaxb]))
	    imaxb = i;
	}
	if (imaxb>=0) {
	  progress[imaxb] = 1;
	  ++s;
	  ++l;
	}
      }
    }
    if (s<2*N)
      cout << "Case #" << c << ": Too Bad" << endl;
    else
      cout << "Case #" << c << ": " << l << endl;
  }
  return 0;
}
