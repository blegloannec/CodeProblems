#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;



int main () {
  int b1,b2,b3,g1,g2,g3,c1,c2,c3;
  while (scanf("%d %d %d %d %d %d %d %d %d",&b1,&g1,&c1,&b2,&g2,&c2,&b3,&g3,&c3) > 0) {
    //printf("%d %d %d %d %d %d %d %d %d\n",b1,g1,c1,b2,g2,c2,b3,g3,c3);
    int min_mv,mouv;
    char *min_str = (char*) malloc(3*sizeof(char));
    // Cas BCG
    strcpy(min_str,"BCG");
    min_mv = b2+b3+c1+c3+g1+g2;
     mouv = 0;
    // BGC
    mouv = b2+b3+g1+g3+c1+c2;
    // printf("%d\n",mouv);
    if (mouv < min_mv) {
      min_mv = mouv;
      strcpy(min_str,"BGC");
    }
    // CBG
    mouv = c2+c3+b1+b3+g1+g2;
    // printf("%d\n",mouv);
    if (mouv < min_mv) {
      min_mv = mouv;
      strcpy(min_str,"CBG");
    }
    // CGB
    mouv = c2+c3+g1+g3+b1+b2;
    if (mouv < min_mv) {
      min_mv = mouv;
      strcpy(min_str,"CGB");
    }
    // GBC
    mouv = g2+g3+b1+b3+c1+c2;
    if (mouv < min_mv) {
      min_mv = mouv;
      strcpy(min_str,"GBC");
    }
    // GCB
    mouv = g2+g3+c1+c3+b1+b2;
    if (mouv < min_mv) {
      min_mv = mouv;
      strcpy(min_str,"GCB");
    }
    printf("%s %d\n",min_str,min_mv);
  }
  return 0;
}
