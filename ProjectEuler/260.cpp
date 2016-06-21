#include <iostream>
using namespace std;

// NB: c'est un 3-heap Wythoff's game
// mais cela n'aide pas à la résolution du pb

const int N = 1001;
bool W[N][N][N];

void sort3(int &x, int &y, int &z) {
  if (y<x) swap(x,y);
  if (z<x) swap(x,z);
  if (z<y) swap(y,z);
}

int main() {
  for (int x=0; x<N; ++x)
    for (int y=x; y<N; ++y)
      for (int z=y; z<N; ++z)
	W[x][y][z] = false;
  int cpt = 0;
  /* On code la progdyn du jeu façon crible.
     Tres efficace car on ne "propage" que depuis les positions
     perdantes, et, dans ce jeu, il y en a beaucoup moins
     que de positions gagnantes (ce qui est intuitif dans la
     mesure où le nb de positions accessibles depuis une conf
     est assez grand, ou autrement dit les degrés dans l'arène
     sont assez élévés, ce qui déséquilibre le jeu en faveur du
     premier joueur).
  */
  for (int x=0; x<N; ++x)
    for (int y=x; y<N; ++y)
      for (int z=y; z<N; ++z)
	if (!W[x][y][z]) {
	  cpt += x+y+z;
	  // position perdante, on crible les positions gagnantes
	  // depuis lesquelles on peut l'atteindre
	  for (int dx=1; x+dx<N; ++dx) {
	    int x0=x+dx, y0=y, z0=z;
	    sort3(x0,y0,z0);
	    W[x0][y0][z0] = true;
	  }
	  for (int dy=1; y+dy<N; ++dy) {
	    W[x][min(y+dy,z)][max(y+dy,z)] = true;
	    int x0=x+dy, y0=y+dy, z0=z;
	    sort3(x0,y0,z0);
	    W[x0][y0][z0] = true;
	  }
	  for (int dz=1; z+dz<N; ++dz) {
	    W[x][y][z+dz] = true;
	    W[min(x+dz,y)][max(x+dz,y)][z+dz] = true;
	    W[x][y+dz][z+dz] = true;
	    W[x+dz][y+dz][z+dz] = true;
	  }
	}
  cout << cpt << endl;
  return 0;
}
