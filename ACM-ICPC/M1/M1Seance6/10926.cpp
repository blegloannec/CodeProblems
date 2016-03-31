#include <iostream>
#include <vector>

using namespace std;

vector<int> graph[105];
int fils[105];
int deg[105];
bool visit[105];
int nbfils;

void compute(int x){
  visit[x]=true;
  nbfils++;
  for(int i=0;i<(int) graph[x].size();++i)
    if (!(visit[graph[x][i]]))
      compute(graph[x][i]);
}

int main(){
  int n, arr, tmp;
  cin >> n;
  while(n!=0){
    for (int i=0;i<n;++i){
      fils[i]=-1;
      graph[i].clear();
      deg[i]=0;
    }
    for (int i=0;i<n;++i){
      cin >> arr;
      for(int j=0;j<arr;++j){
	cin >> tmp;
	--tmp;
	deg[tmp]++;
	graph[i].push_back(tmp);
      }
    }
    for(int i=0;i<n;++i)
      if (deg[i]==0){
	for(int j=0;j<n;++j)
	  visit[j]=false;
	nbfils=0;
	compute(i);
	fils[i]=nbfils;
      }
    int res=0;
    for (int i=1;i<n;++i)
      if (deg[i]==0 && fils[i]>fils[res])
	res= i;
    cout << (res+1) << '\n';
    cin >> n;
  }
}
