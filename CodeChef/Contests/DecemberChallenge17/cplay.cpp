#include <cstdio>
using namespace std;

char P[20];

int penalty(int &k) {
  int s[2], r[2];
  s[0] = s[1] = 0;
  r[0] = r[1] = 5;
  for (int i=0; i<10; ++i) {
    int ti = i&1;
    if (P[i]=='1') ++s[ti];
    --r[ti];
    for (int t=0; t<2; ++t)
      if (s[t]>s[t^1]+r[t^1]) {
	k = i+1;
	return t+1;
      }
  }
  for (int i=10; i<20; ++i) {
    int ti = i&1;
    if (P[i]=='1') ++s[ti];
    if (i&1)
      for (int t=0; t<2; ++t)
	if (s[t]>s[t^1]) {
	  k = i+1;
	  return t+1;
	}
  }
  return 0;
}

int main() {
  while (scanf("%s",P)==1) {
    int k;
    int w = penalty(k);
    if (w==0) printf("TIE\n");
    else if (w==1) printf("TEAM-A %d\n",k);
    else printf("TEAM-B %d\n",k);
  }
  return 0;
}
