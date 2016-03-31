#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> paire;

queue<paire> q;

char tab[26][26];

int n;
int x;
int y;

void found(){
  x=-1; y=-1;
  for (int i=0;i<n;++i)
    for (int j=0;j<n;++j)
      if (tab[i][j]=='1'){
	x=i;
	y=j;
      }
}

void destruct(){
  q.push(paire(x, y));
  int a, b;
  while (!q.empty()){
    a= q.front().first;
    b= q.front().second;
    q.pop();
    tab[a][b]=0;
    if (a-1>=0 && b-1>=0 && tab[a-1][b-1]=='1')
      q.push(paire(a-1,b-1));
    if (a-1>=0 && tab[a-1][b]=='1')
      q.push(paire(a-1,b));
    if (a-1>=0 && b+1<n && tab[a-1][b+1]=='1')
      q.push(paire(a-1,b+1));
    if (b-1>=0 && tab[a][b-1]=='1')
      q.push(paire(a,b-1));
    if (b+1<n && tab[a][b+1]=='1')
      q.push(paire(a,b+1));
    if (a+1<n && b-1>=0 && tab[a+1][b-1]=='1')
      q.push(paire(a+1,b-1));
    if (a+1<n && tab[a+1][b]=='1')
      q.push(paire(a+1,b));
    if (a+1<n && b+1<n && tab[a+1][b+1]=='1')
      q.push(paire(a+1,b+1));
  }
}

int main(){
  int cas=1;
  int res=0;
  while (cin >> n){
    res=0;
    for (int i=0;i<n;++i)
      for (int j=0;j<n;++j){
	cin >> tab[i][j];
      }
    /*
    for (int i=0;i<n;++i){
      for (int j=0;j<n;++j)
	cout << tab[i][j] << ' ';
      cout << '\n';
}
    */
    found();
    while(!q.empty())
      q.pop();
    while (x!=-1){
      //cout << "je suis la \n";
      destruct ();
      found();
      res++;
    }
    cout << "Image number " << cas << " contains " << res << " war eagles.\n";
    ++cas;
  }
}
