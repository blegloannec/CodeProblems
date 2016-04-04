#include <iostream>
using namespace std;

typedef long long ent;

/*
  Relations pour le nb *total* de cubes en 2D
def Crec(x,y,n):
    return x*y if n==0 else Crec(x,y,n-1)+2*(x+y)+4*(n-1)

def C(x,y,n):
    return x*y+2*(x+y)+2*(x+y+n)*(n-1)
*/

// En 3D :
// nb cubes layer n(>1) = z*(C(x,y,n)-C(x,y,n-1))+2*C(x,y,n-1)
// Apres simplification :
ent D(ent x, ent y, ent z, ent n) {
  return 2*(x*y+x*z+y*z) + 4*(x+y+z+n-2)*(n-1);
}

const int N = 100000;
int cpt[N];
const int C = 1000;

int main() {
  for (int i=0; i<N; ++i) cpt[i] = 0;
  for (int x=1; x<N; ++x)
    for (int y=x; x*y<N; ++y)
      for (int z=y; D(x,y,z,1)<N; ++z)
	for (int n=1; n<N; ++n) {
	  ent d = D(x,y,z,n);
	  if (d>N) break;
	  ++cpt[d];
	}

  for (int i=0; i<N; ++i)
    if (cpt[i]==C) {
      cout << i << endl;
      break;
    }
  
  return 0;
}
