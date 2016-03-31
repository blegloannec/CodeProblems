#include <iostream>
using namespace std;

long long L, amin, amax, bmin, bmax;

char solve()
{
	long long d, q;

	if (L <= amax)
		return 'A';

	d = amax - amin + bmin - bmax;
	q = (L - 1) / (amin + bmax);

	if (d < 0 && q > ((bmax - bmin - amax + d + 1) / d))
		return 'B';

	return (((L - 1) % (amin + bmax)) < (amax + q * d)) ? 'A' : 'B';
}

int main() {
  int n;
  cin >> n;
  while (n-->0) {
    cin >> L >> amin >> amax >> bmin >> bmax;
    cout << solve() << '\n';
  }
  return 0;
}
