// 10142

#include <iostream>
#include <list>
#include <cstring>
#include <cstdio>
using namespace std;

#define MAX 21
#define MAXV 1001

char names[MAX][101];
bool elim[MAX];
list<int> vote[MAXV];
int score[MAX];
list<int> vires;
int n;

int main() {
  int cas,nbv,mini,nbc,winner,maxscore,m,v,curr;
  char buff[100];
  list<int>::iterator it;
  bool debut = true;
  cin >> cas;
  while (cas-->0) {
    if (debut) debut = false;
    else cout << '\n';
    cin >> n;
    cin.ignore();
    for (int i=0; i<n; ++i)
      cin.getline(names[i],sizeof(names[i]));
    cin.getline(buff,sizeof(buff));
    nbv = 0;
    while ((buff[0]!=0)&&(buff[0]!='\n')) {
      curr = 0;
      m = 0;
      v = 0;
      while (m<n) {
	if (*(buff+curr)==' ') {
	  vote[nbv].push_back(v-1);
	  v = 0;
	  ++m;
	  ++curr;
	  if (m<n) 
	    while (*(buff+curr)==' ') ++curr;
	  else break;
	}
	else {
	  v = 10*v + (*(buff+curr) - '0');
	  ++curr;
	}
      }
      cin.getline(buff, sizeof(buff));
      ++nbv;
    }
    for (int k=0; k<n; ++k)
      elim[k] = false;
    nbc = n;
    while (nbc > 1) {
      for (int i=0; i<n; ++i)
	score[i] = 0;
      maxscore = 0;
      winner = 0;
      for (int i=0; i<nbv; ++i) {
	while (elim[vote[i].front()]) vote[i].pop_front();
	++score[vote[i].front()];
	if (score[vote[i].front()] > maxscore) {
	  maxscore = score[vote[i].front()];
	  winner = vote[i].front();
	}
      }
      if (maxscore > nbv/2) { // un gagnant
	nbc = 0;
	vires.clear();
	vires.push_back(winner);
	break;
      }
      mini = MAXV+1;
      for (int i=0; i<n; ++i) 
	if ((!elim[i])&&(mini>score[i])) mini = score[i];
      vires.clear();
      for (int i=0; i<n; ++i) 
	if ((!elim[i])&&(score[i]==mini)) {
	  elim[i] = true;
	  vires.push_back(i);
	  --nbc;
	}
    }
    if (nbc == 0) { // egalite
      for (it=vires.begin(); it!=vires.end(); it++) 
	cout << names[*it] << '\n';
    }
    else { // un gagnant
      for (int i=0; i<n; ++i) 
	if (!elim[i]) {
	  cout << names[i] << "\n";
	  break;
	};
    }
    for (int i=0; i<nbv; ++i) 
      vote[i].clear();
  }

  return 0;
}
