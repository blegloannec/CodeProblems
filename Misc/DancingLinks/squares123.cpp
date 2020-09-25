/*
  http://images.math.cnrs.fr/Septembre-2020-4e-defi.html
  Paver un carré 23x23 avec des carrés 1x1, 2x2 et 3x3
  Minimiser les 1x1
*/
#include <cstdio>
#include <cstdlib>
#include <vector>
#include "dancing_links.h"
using namespace std;

#define P(X,Y) ((X)*L+(Y))
#define LAST1(N) (H*L+(N))

const int H = 23;
const int L = H;
int nb1 = 1;  // nb of 1x1 to use (exactly)
subsets S;

void gen() {
  for (int i=0; i<H; ++i)
    for (int j=0; j<L; ++j) {
      for (int d=3; d>=2; --d)
	if (i+d<=H && j+d<=L) {
	  subset s;
	  for (int a=0; a<d; ++a)
	    for (int b=0; b<d; ++b)
	      s.push_back(P(i+a,j+b));
	  S.push_back(s);
	}
      for (int n=0; n<nb1; ++n) {
	subset s {P(i,j), LAST1(n)};
	S.push_back(s);
      }
    }
}

void svg(const vector<int> &sol) {
  int A = 15;
  printf("<svg width=\"%d\" height=\"%d\">\n", A*L, A*H);
  for (int i : sol) {
    int y = S[i][0]/L, x = S[i][0]%L;
    int c = 1;
    char *col = (char*)("rgb(255,100,100)");
    if (S[i].size()==4) {
      c = 2;
      col = (char*)"rgb(200,255,200)";
    }
    else if (S[i].size()==9) {
      c = 3;
      col = (char*)"rgb(200,200,255)";
    }
    printf("<rect x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\" style=\"fill: %s; stroke: black; stroke-width: 3;\" />\n", A*x, A*y, A*c, A*c, col);
  }
  printf("</svg>\n");
}

int main(int argc, char **argv) {
  if (argc>1) nb1 = atoi(argv[1]);
  int size = H*L + nb1;
  gen();
  vector<int> sol;
  if (dancing_links(size, S, sol)) svg(sol);
  else fprintf(stderr, "NO SOLUTION\n");
  return 0;
}
