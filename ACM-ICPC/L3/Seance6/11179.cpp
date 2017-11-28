#include <cstdio>
#include <vector>
using namespace std;

typedef unsigned long long ent;

int main() {
  int cas = 1;

  while (true) {
    // input reading
    int b;
    ent L,n,m,C;
    scanf("%Ld",&L);
    if (L==0) break;
    scanf("%d %Ld %Ld %Ld",&b,&n,&m,&C);

    int bit = 0, r, max_chunk_nb = 2;
    ent l = 0;
    vector<int> BS;
    scanf("%d",&r);
    if (r==0) bit = 1;
    else {
      BS.push_back(r);
      l += r;
      max_chunk_nb = max(max_chunk_nb,r/b+1);
    }
    scanf("%d",&r);
    while (r>0) {
      BS.push_back(r);
      l += r;
      max_chunk_nb = max(max_chunk_nb,r/b+1);
      scanf("%d",&r);
    }

    // size check
    if (l!=L) {
      printf("Bitstream %d: Invalid Length\n",cas++);
      continue;
    }

    // computing checksum
    // pre-computations
    vector<ent> pown(max_chunk_nb,1), pow1(max_chunk_nb,0);
    ent chunk1 = (1LL<<b)-1;
    for (int i=1; i<max_chunk_nb; ++i) {
      pown[i] = (pown[i-1]*n)%m;
      pow1[i] = (pow1[i-1]*n + chunk1)%m;
    }
    // actual computation in O(nb of blocks)
    ent c = 0, chunk = 0;
    int s = 0;
    for (unsigned int i=0; i<BS.size(); ++i) {
      int rs = BS[i];
      // completing current chunk
      while (s<b && rs>0) {
	chunk = (chunk<<1) | bit;
	++s;
	--rs;
      }
      if (s==b) {
	c = (c*n + chunk)%m;
	chunk = 0;
	s = 0;
      }
      // processing all full-bit chunks of the block at once
      if (rs>0) {
	int p = rs/b;
	c = (c*pown[p] + (bit ? pow1[p] : 0))%m;
	rs %= b;
	if (bit) chunk = (1LL<<rs)-1;
	s = rs;
      }
      bit = 1-bit;
    }
    // final padding
    if (s>0) {
      chunk <<= b-s;
      c = (c*n + chunk)%m;
    }

    // output
    if (c==C) printf("Bitstream %d: Compression OK\n",cas++);
    else printf("Bitstream %d: Invalid Checksum\n",cas++);
  }

  return 0;
}
