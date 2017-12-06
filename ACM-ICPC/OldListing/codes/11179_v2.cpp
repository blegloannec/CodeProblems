/* 11179 Bit Stream
   Version 2
   Ce programme calcule les checksums seulement si la 
   longueur est verifiee juste au prealable.
*/
   

#include <iostream>
#include <cmath>
using namespace std;

#define MAX 100000
#define INTMAX 0xffffffff

int flux[MAX];
int b,cur_puis,taille_flux;
unsigned int cur_int,cur_int_max;
unsigned long long n,m,cur_sum,C,L;

void hasher(int bit) { // Calcule la checksum a la volee
  cur_int = 2*cur_int + bit;
  if (cur_puis == 0) {
    cur_sum = (cur_sum*n + cur_int) % m;
    cur_int = 0;
    cur_puis = b;
  }
  else --cur_puis;
}

void calc_checksum() {
  int cur_bit = 0;
  int in;
  cur_sum = 0;
  cur_puis = b;
  cur_int = 0;

  for (int i=0; i<taille_flux; i++) {
    in = flux[i];
    while (in > 0) {
      if ((cur_puis==b)&&(in>b)) {
	if (cur_bit==0) cur_sum = (cur_sum*n) % m;
	else cur_sum = (cur_sum*n + cur_int_max) % m;
	in -= b+1;
      }
      else {
	hasher(cur_bit);
	--in;
      }
    }
    cur_bit = (cur_bit+1)%2;
  }

  // On complete avec des 0
  while (cur_puis != b) hasher(0);
}

int main() {
  int cpt,in;
  unsigned long long l;
  cpt = 0;

  while (cin >> L) {
    if (L==0) return 0;
    cin >> b >> n >> m >> C;
    if (b==32) cur_int_max = INTMAX;
    else cur_int_max = (unsigned int)pow(2,(float)b)-1;
    --b; // ATTENTION b := b-1
    n = n%m; // allege eventuellement les calculs

    taille_flux = 1;
    cin >> in;
    l = in;
    flux[0] = in;
    cin >> in;
    while (in!=0) {
      l += in;
      if (l>L) {
	cin >> in;
	while (in!=0) cin >> in;
	break;
      }
      flux[taille_flux++] = in;
      cin >> in;
    }

    if (l != L) {
      cout << "Bitstream " << ++cpt << ": Invalid Length\n";
      continue;
    }

    calc_checksum();
    
    if (cur_sum == C) cout << "Bitstream " << ++cpt << ": Compression OK\n";
    else cout << "Bitstream " << ++cpt << ": Invalid Checksum\n";

  }

  return 0;
}
