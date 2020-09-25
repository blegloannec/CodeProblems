/*
  Jean-Paul DELAHAYE, Formes et ensembles autopavables, PLS 277, 12/2016
  http://cristal.univ-lille.fr/~jdelahay/pls/2016/277.pdf
  Paver un carré 23x24 avec des polyominos #####
                                            #
*/
#include <iostream>
#include <vector>
#include "dancing_links.h"
using namespace std;

#define P(X,Y) ((X)*L+(Y))

const int H = 23;
const int L = 24;

void gen(subsets &res) {
  for (int i=0; i<H; ++i)
    for (int j=0; j<L; ++j) {
      if (j<L-4 && i<H-1) {
	subset s1 {P(i,j),P(i,j+1),P(i,j+2),P(i,j+3),P(i,j+4),P(i+1,j+1)};
	res.push_back(s1);
	subset s2 {P(i,j),P(i,j+1),P(i,j+2),P(i,j+3),P(i,j+4),P(i+1,j+3)};
	res.push_back(s2);
      }
      if (j<L-4 && i>0) {
	subset s3 {P(i,j),P(i,j+1),P(i,j+2),P(i,j+3),P(i,j+4),P(i-1,j+1)};
	res.push_back(s3);
	subset s4 {P(i,j),P(i,j+1),P(i,j+2),P(i,j+3),P(i,j+4),P(i-1,j+3)};
	res.push_back(s4);
      }
      if (i<H-4 && j<L) {
	subset s5 {P(i,j),P(i+1,j),P(i+2,j),P(i+3,j),P(i+4,j),P(i+1,j+1)};
	res.push_back(s5);
	subset s6 {P(i,j),P(i+1,j),P(i+2,j),P(i+3,j),P(i+4,j),P(i+3,j+1)};
	res.push_back(s6);
      }
      if (i<H-4 && j>0) {
	subset s7 {P(i,j),P(i+1,j),P(i+2,j),P(i+3,j),P(i+4,j),P(i+1,j-1)};
	res.push_back(s7);
	subset s8 {P(i,j),P(i+1,j),P(i+2,j),P(i+3,j),P(i+4,j),P(i+3,j-1)};
	res.push_back(s8);
      }
    }
}

int main() {
  subsets s;
  gen(s);
  vector<int> sol;
  dancing_links(H*L,s,sol);
  cout << sol.size() << endl;
  return 0;
}
