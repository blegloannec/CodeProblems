#include <iostream>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;

char tourname[200];
int nbequipe;

struct team{
  string name;
  int points;
  int wins;
  int ties;
  int losses;
  int goalscored;
  int goalagainst;
  team(string a): name(a), points(0), wins(0), ties(0), losses(0), goalscored(0), goalagainst(0) {}
 team(): name(""), points(0), wins(0), ties(0), losses(0), goalscored(0), goalagainst(0) {}
};

bool tri(team a, team b){
  char tmp1[sizeof(a.name)];
  char tmp2[sizeof(b.name)];

  for (int i=0;i<sizeof(a.name);++i)
    tmp1[i]= a.name[i];

  for (int i=0;i<sizeof(b.name);++i)
    tmp2[i]= b.name[i];

  return
    (a.points > b.points)
    || ((a.points== b.points) && (a.wins> b.wins))
    || ((a.points== b.points) && (a.wins == b.wins) && ((a.goalscored-a.goalagainst) > (b.goalscored-b.goalagainst)))
    || ((a.points== b.points) && (a.wins == b.wins) && ((a.goalscored-a.goalagainst) == (b.goalscored-b.goalagainst)) && (a.goalscored > b.goalscored))
    || ((a.points== b.points) && (a.wins == b.wins) && ((a.goalscored-a.goalagainst) == (b.goalscored-b.goalagainst)) && (a.goalscored == b.goalscored) && ((a.wins+ a.ties+ a.losses) < (b.wins+ b.ties+ b.losses)))
    ||  ((a.points== b.points) && (a.wins == b.wins) && ((a.goalscored-a.goalagainst) == (b.goalscored-b.goalagainst)) && (a.goalscored == b.goalscored) && ((a.wins+ a.ties+ a.losses) == (b.wins+ b.ties+ b.losses)) && (strcasecmp(tmp1,tmp2)<0));
}

map<string,team> tab;
team tabl[32];

int main(){
  int cas, nbmatch;
  char team1[200], team2[200];
  int score1, score2;
  char tmp[200];
  cin >> cas;
  cin.ignore();
  while(cas-->0){
    cin.getline(tourname, 200);
    cin >> nbequipe;
    cin.ignore();
    for (int i=0;i<nbequipe;++i){
      cin.getline(tmp, 200);
      tab.insert(pair<string,team>(tmp, team(tmp)));
    }
    cin >> nbmatch;
    cin.ignore();
    while(nbmatch-->0){
      scanf("%[^#]#%d@%d#%[^#^\n]\n",team1, &score1, &score2, team2);
      tab[team1].goalscored += score1;
      tab[team2].goalscored += score2;
      tab[team1].goalagainst += score2;
      tab[team2].goalagainst += score1;
      if (score1> score2){
	tab[team1].wins++;
	tab[team1].points+=3;
	tab[team2].losses++;
      }
      else if (score1==score2){
	tab[team1].ties++;
	tab[team1].points++;
	tab[team2].ties++;
	tab[team2].points++;
      }
      else{
	tab[team2].wins++;
	tab[team2].points+=3;
	tab[team1].losses++;
      }
    }
    map<string, team>::iterator it;
    int curr=0;
    for (it=tab.begin(); it!= tab.end(); ++it)
      tabl[curr++]= it->second;

    sort(tabl, tabl+nbequipe, tri);

    cout << tourname << '\n';
    for (int i=0;i< nbequipe; ++i){
      printf("%d) ",i+1);
      cout << tabl[i].name;
      printf(" %dp, %dg (%d-%d-%d), %dgd (%d-%d)\n", tabl[i].points, tabl[i].wins+ tabl[i].ties+ tabl[i].losses, tabl[i].wins, tabl[i].ties, tabl[i].losses, tabl[i].goalscored- tabl[i].goalagainst, tabl[i].goalscored, tabl[i].goalagainst);
    }
    tab.clear();
    if (cas>0)
      cout << '\n';
  }
}
