#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;

#define MAX 10000

typedef vector<int> liste;

int P,N,nb,auts,erdos;
string s;
int rang[MAX];
liste t[MAX];
map<string,int> auth;
char buff[MAX];

void BFS() {
  queue<int> q;
  int curr;
  liste::iterator it;
  for (int i=0; i<nb; i++) rang[i]=-1;
  rang[erdos] = 0;
  q.push(erdos);
  while (!q.empty()) {
    curr = q.front(); q.pop();
    for (it=t[curr].begin(); it!=t[curr].end(); ++it) {
      int d = *it;
      if (rang[d]<0) {
	q.push(d);
	rang[d] = rang[curr]+1;
      }
    }
  }
}

void ajoute() {
  map<string,int>::iterator it = auth.find(s);
  if (it==auth.end()) {
    auth.insert(pair<string,int>(s,nb));
    rang[auts] = nb;
    if (s=="Erdos, P.") erdos = nb;
    ++auts;
    ++nb;
  }
  else {
    rang[auts] = it->second;
    ++auts;
  }
}

int main() {
  int n,tmp,pos;
  bool bs;

  cin >> n;
  
  for (int cas=1; cas<=n; ++cas) {
    cin >> P >> N;
    tmp = 0;
    nb = 0;    

    cin.getline(buff,sizeof(buff));
    for (int p=0; p<P; p++) {
      while (true) {
	pos = 0;
	cin.getline(buff,sizeof(buff));
	while (buff[pos]==' ') ++pos;
	if ((buff[pos]!='\0')&&(buff[pos]!='\n')) break;
      }
      tmp = 0;
      auts = 0;
      s = "";
      bs = false;
      while (buff[pos]!=':') {
	if (buff[pos]==',') {
	  if (tmp==1) {
	    tmp = 0;
	    ajoute();
	    ++pos;
	    s = "";
	  }
	  else {
	    ++tmp;
	    s += buff[pos];
	  }
	}
	else {
	  if (!bs) {
	    s += buff[pos];
	    bs = (buff[pos]==' ');
	  }
	  else if (buff[pos]!=' ') {
	    bs = false;
	    s += buff[pos];
	  }
	}
	++pos;
      }
      ajoute();

      for (int i=0; i<auts; i++) 
	for (int j=i+1; j<auts; j++) {
	  t[rang[i]].push_back(rang[j]);
	  t[rang[j]].push_back(rang[i]);
	}
      
    }
    
    BFS();

    map<string,int>::iterator it;
   
    cout << "Scenario " << cas << '\n';
    for (int p=0; p<N; p++) {
      cin.getline(buff,sizeof(buff));
      s = string(buff);
      it = auth.find(s);
      cout << s << ' ';
      if (rang[it->second]<0) cout << "infinity\n";
      else cout << rang[it->second] << '\n';
    }
    
    auth.clear();
    for (int i=0; i<auts; ++i) t[i].clear();
  }
  
  return 0;
}
