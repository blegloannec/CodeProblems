#include <cstdio>
#include <cstdlib>
#include <cstring>

int getGame(char *lang, char* g) {
  if (!strcmp(lang,"cs")) {
    if (!strcmp(g,"Kamen")) return 1;
    else if (!strcmp(g,"Nuzky")) return 2;
    else return 3;
  }
  else if (!strcmp(lang,"en")) {
    if (!strcmp(g,"Rock")) return 1;
    else if (!strcmp(g,"Scissors")) return 2;
    else return 3;
  }
  else if (!strcmp(lang,"fr")) {
    if (!strcmp(g,"Pierre")) return 1;
    else if (!strcmp(g,"Ciseaux")) return 2;
    else return 3;
  }
  else if (!strcmp(lang,"de")) {
    if (!strcmp(g,"Stein")) return 1;
    else if (!strcmp(g,"Schere")) return 2;
    else return 3;
  }
  else if (!strcmp(lang,"hu")) {
    if (!strcmp(g,"Papir")) return 3;
    else if ((!strcmp(g,"Ko")) || (!strcmp(g,"Koe"))) return 1;
    else return 2;
  }
  else if (!strcmp(lang,"it")) {
    if (!strcmp(g,"Forbice")) return 2;
    else if ((!strcmp(g,"Rete")) || (!strcmp(g,"Carta"))) return 3;
    else return 1;
  }
  else if (!strcmp(lang,"jp")) {
    if (!strcmp(g,"Guu")) return 1;
    else if (!strcmp(g,"Paa")) return 3;
    else return 2;
  }
  else if (!strcmp(lang,"pl")) {
    if (!strcmp(g,"Kamien")) return 1;
    else if (!strcmp(g,"Papier")) return 3;
    else return 2;
  }
  else {
    if (!strcmp(g,"Papel")) return 3;
    else if (!strcmp(g,"Piedra")) return 1;
    else return 2;
  }
}

int main(void) {
  char *name1 = (char*) malloc(30*sizeof(char));
  char *name2 = (char*) malloc(30*sizeof(char));  
  char *lang1 = (char*) malloc(3*sizeof(char));
  char *lang2 = (char*) malloc(3*sizeof(char));
  char *g1 = (char*) malloc(20*sizeof(char));
  char *g2 = (char*) malloc(20*sizeof(char));
  bool test = true;
  bool test2;
  int s1,s2,p1,p2,nbgame;
  nbgame = 1;

  while (test) {
    scanf("%s %s", lang1, name1);
    scanf("%s %s", lang2, name2);
    s1 = 0;
    s2 = 0;
    test2 = true;
    while (test2) {
      scanf("%s",g1);
      if (!strcmp(g1,"-")) test2 = false;
      else if (!strcmp(g1,".")) {
	test = false;
	test2= false;
      }
      else {
	scanf("%s",g2);
	p1 = getGame(lang1,g1);
	p2 = getGame(lang2,g2);
	if (p1==1) {
	  if (p2==2) ++s1;
	  else if (p2==3) ++s2;
	}
	else if (p1==2) {
	  if (p2==1) ++s2;
	  else if (p2==3) ++s1;
	}
	else {
	  if (p2==1) ++s1;
	  else if (p2==2) ++s2;
	}
      }
    }
    
    printf("Game #%d:\n",nbgame++);
    printf("%s: %d ",name1,s1);
    if (s1==1) printf("point\n");
    else printf("points\n");
    printf("%s: %d ",name2,s2);
    if (s2==1) printf("point\n");
    else printf("points\n");
    if (s1>s2) printf("WINNER: %s\n\n",name1);
    else if (s2>s1) printf("WINNER: %s\n\n",name2);
    else printf("TIED GAME\n\n");

  }  

  return 0;
}
