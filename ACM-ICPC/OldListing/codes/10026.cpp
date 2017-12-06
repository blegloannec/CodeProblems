#include <iostream>
#include <algorithm>

using namespace std;



struct tache{
  int time;
  int fine;
  int ind;
  tache (int a, int b, int c): time(a), fine(b), ind(c) {};
  tache():time(0), fine(0), ind(0) {};
};

bool comp(tache a, tache b){
  return (b.time*a.fine- a.time*b.fine)>0;
}

tache tab[1001];

int main(){
  int cas, scas;
  int tmpa, tmpb;
  bool h=true;
  cin >> cas;
  while(cas-->0){
    if(!h)
      cout << '\n';
    else
      h=false;
    cin >> scas;
    for (int i=0;i<scas;++i){
      cin >> tmpa >> tmpb;
      tab[i]= tache(tmpa, tmpb, i+1);
    }

    sort(tab, tab+ scas, comp);

    for (int i=0;i<scas-1;++i)
      cout << tab[i].ind << ' ';
    cout << tab[scas-1].ind;
    cout << '\n';

  }
}
