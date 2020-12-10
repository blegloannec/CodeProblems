#include <cstdio>
using namespace std;

struct Link {
  char c;
  Link *L, *R;
  Link(char c, Link *L=NULL, Link *R=NULL) : c(c), L(L), R(R) {}
};

Link *link_ins(char c, Link *X) {
  Link *Y = new Link(c, X, X->R);
  X->R = Y;
  if (Y->R!=NULL) Y->R->L = Y;
  return Y;
}

Link *link_del(Link *X) {
  Link *Y = X->L;
  Y->R = X->R;
  if (Y->R!=NULL) Y->R->L = Y;
  delete X;
  return Y;
}

int main() {
  Link *head = new Link('^');
  Link *curr = head;
  char c;
  while (scanf("%c", &c)==1 && c!='\n') {
    if      (c=='L') curr = curr->L;
    else if (c=='R') curr = curr->R;
    else if (c=='B') curr = link_del(curr);
    else             curr = link_ins(c, curr);
  }
  while (head->R!=NULL) {
    head = head->R;
    printf("%c", head->c);
  }
  printf("\n");
  return 0;
}
