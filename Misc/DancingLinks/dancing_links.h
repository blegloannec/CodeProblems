#include <vector>
using namespace std;

typedef vector<int> subset;
typedef vector<subset> subsets;

bool dancing_links(int size, const subsets &sets, vector<int> &sol);
int dancing_links_count(int size, const subsets &sets);
