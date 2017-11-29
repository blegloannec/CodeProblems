// H. Small Factors

#include <iostream>
#include <limits.h>

using namespace std;

unsigned puiss3[] = {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467};

int main(int argc, char *argv[])
{
  unsigned m, min;
  int j;

  while (cin >> m && m) {
    min = UINT_MAX;
    for (int i = 0; i < 20; ++i) {
      for (j = 0; (puiss3[i] << j) < m; ++j);
      if ((puiss3[i] << j) < min) min = puiss3[i] << j;
    }
    cout << min << '\n';
  }

  return 0;
}
