// http://oeis.org/A108235

#include <iostream>
#include "dancing_links.h"
using namespace std;

int main() {
  int size = 36;
  subsets Triples;
  for (int i=1; i<=size; ++i)
    for (int j=i+1; i+j<=size; ++j) {
      subset Triple {i-1,j-1,i+j-1};
      Triples.push_back(Triple);
    }
  cout << dancing_links_count(size,Triples) << endl;
  return 0;
}
