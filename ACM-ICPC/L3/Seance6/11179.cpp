/* 11179 Bit Stream
   Ce programme calcule les checksums a la volee
   Ce qui est trop lent quand on utilise des long long,
   ce qui est imposé par les bornes enormes des donnees
   du probleme.
*/
   
#include <cstdio>
#include <iostream>
using namespace std;

typedef unsigned long long ent;

int b,cur_puis;
ent n,m,cur_sum,cur_int,C,L;

void hasher(int bit) { // Calcule la checksum a la volee
  cur_int = 2*cur_int + bit;
  if (cur_puis == 0) {
    cur_sum = (cur_sum*n + cur_int) % m;
    cur_int = 0;
    cur_puis = b-1;
  }
  else --cur_puis;
}

int main() {
  int cpt,in,cur_bit;
  ent l;
  cpt = 0;

  while (scanf("%Ld", &L)==1) {
    if (L==0) return 0;
    scanf("%d %Ld %Ld %Ld", &b, &n, &m, &C);

    cur_sum = 0;
    cur_puis = b-1;
    cur_int = 0;
    l = 0;

    scanf("%d", &in);
    l += in;
    while (--in >= 0) hasher(0);

    cur_bit = 1;
    scanf("%d", &in);
    while (in != 0) {
      l += in;
      while (--in >= 0) hasher(cur_bit);
      cur_bit = (cur_bit+1)%2;
      scanf("%d", &in);
    }

    if (l != L) {
      printf("Bitstream %d: Invalid Length\n", ++cpt);
      continue;
    }

    // On complete avec des 0
    while (cur_puis != b-1) hasher(0);
    
    if (cur_sum == C) printf("Bitstream %d: Compression OK\n", ++cpt);
    else printf("Bitstream %d: Invalid Checksum\n", ++cpt);

  }

  return 0;
}
