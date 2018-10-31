#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

/* 
   Amelioration et simplification de 1B.chefko.cpp
   Pour chaque t, si l'on connait les intervalles couvrant t,
   et que l'on note t' la K-ieme plus grande borne droite d'un
   de ces intervalles en partant de la fin (si elle existe),
   alors [t,t'] est le plus grand intervalle partant de t a etre
   couvert par au moins K intervalles.
   Vu comme cela t' peut etre calcule en maintenant un tas-min
   de taille <=K contenant a chaque instant t les K plus grandes
   bornes droites des intervalles couvrant t.
   Le cout est O(n log n) pour le tri (puis calcul en O(n log k)).
*/

int main() {
  int T;
  scanf("%d",&T);
  for (int t=0; t<T; ++t) {
    int N,K;
    scanf("%d %d",&N,&K);
    vector< pair<int,int> > TL;
    for (int i=0; i<N; ++i) {
      int l,r;
      scanf("%d %d",&l,&r);
      TL.push_back(make_pair(l,r));
    }
    // timeline O(n log n)
    sort(TL.begin(),TL.end());
    // approche O(n log k)
    priority_queue<int> H;
    int i = 0, res = 0;
    while (i<(int)TL.size()) {
      int lt = TL[i].first;
      while (!H.empty() && H.top()==-lt) H.pop();
      while (i<(int)TL.size() && TL[i].first==lt) {
	H.push(-TL[i].second);
	while ((int)H.size()>K) H.pop();
	++i;
      }
      if ((int)H.size()==K) res = max(res,-H.top()-lt);
    }
    printf("%d\n",res);
  }
  return 0;
}
