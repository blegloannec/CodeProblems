// http://oeis.org/A108235
// https://images.math.cnrs.fr/Aout-2018-3e-defi.html
#include <iostream>
#include "dancing_links.h"
using namespace std;

const int size = 39;

int main() {
  subsets Triples;
  for (int i=1; i<=size; ++i)
    for (int j=i+1; i+j<=size; ++j) {
      subset Triple {i-1,j-1,i+j-1};
      Triples.push_back(Triple);
    }
  cout << dancing_links_count(size,Triples) << endl;
  return 0;
}
