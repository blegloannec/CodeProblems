#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#define MAX 2000

using namespace std;


vector<int> t[MAX];
int pred[MAX];
int n;

void DFS(int start, int inter) {
  for (int j=0;j<t[start].size();++j) {
    int d = t[start][j];
    if (d!=inter && pred[d]<0) {
      pred[d] = start;  
      DFS(d, inter);
    }
  }
}

void init(int start){
  for (int i=0;i<n;++i)
    pred[i]=-1;
  pred[start]=start;
}

int main(){
   int in,out,i;
   char str[1000],*p;
   
   while(scanf("%d",&n) == 1 && n){
     for (int i=0;i<n;++i)
       t[i].clear();
      while(scanf("%d",&in) && in){
         if(in == 0)
            break;
         
         gets(str);
         p = strtok(str," ");
         
         while(p){
            out = atoi(p);
            p = strtok(NULL," ");
            t[in - 1].push_back(out - 1);
            t[out - 1].push_back(in - 1);
         }
      }
      int res=0;
      for (int i=0;i<n;++i){
	init(i);
	if (t[i].size()>0){
	  pred[t[i][0]]=t[i][0];
	  DFS(t[i][0],i);
	}
	for(int j=0;j<n;++j)
	  if (pred[j]<0){
	    res++;
	    break;
	  }
      }   
      cout << res << '\n';
   }
}
