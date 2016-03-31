#include <iostream>
#include <algorithm>

using namespace std;

int n,k;
int tab[31];
int tab1[16][20000];
int tab2[16][20000];
int ind1[16];
int ind2[16];

//calcul des sommes du premier ensemble
//nb: nombre d'element de la somme
//curr: somme courante
//deb, fin: indice de tab entre lesquels sont les elements
inline void somme1(int deb, int fin){
  int der=0;
  tab1[der++][ind1[0]++]= 0;
  for(int i=deb;i<=fin;++i){
    for (int j=der;j>0;--j)
      for (int k=0;k<ind1[j-1];++k)
	tab1[j][ind1[j]++]= tab1[j-1][k]+tab[i];
    ++der;
  }
}

//rend l'indice du plus petit element plus grand que s dans le tab1[i]
int search1(int ind, int s){
  int deb=0, fin;
  fin=ind1[ind];
  while
    ((!(tab1[ind][(fin+deb)/2]>s && tab1[ind][(fin+deb)/2-1]<=s)) 
     && (fin > deb)){
      if (tab1[ind][(fin+deb)/2]>s)
	fin= (fin+deb)/2;
      else
	deb= (fin+deb)/2+1;
    }
  return (fin+deb)/2;
}


inline int aux1(int fin, int s){
  int res=0;
  int mini= min(n/2,k), maxi= max(0, k-fin/2);
  for (int i=maxi ;i<=mini;++i)
    for (int l=0;l<ind2[k-i];++l)

      for (int j=0;j<ind1[i];++j)
	if (tab1[i][j]+ tab2[k-i][l]> s) ++res;

  return res;
}

//calcul pour une longueur donnée s
//fin indique le dernier element que l'on peut prendre dans tab
inline int aux2(int fin, int s){
  int res=0;
  int mini= min(n/2,k), maxi= max(0, k-fin/2);
  for (int i=maxi ;i<=mini;++i)
    for (int l=0;l<ind2[k-i];++l)
      res+= ind1[i]-search1(i,s-tab2[k-i][l]);

  return res;
}

int main(){
  int T,res;
  cin >> T;
  for(int cas=1; cas<=T;++cas){
    cin >> n >> k;
    for (int i=0;i<n;++i)
      cin >> tab[i];
    sort(tab, tab+n);
    res=0;
    k--;
    for (int i=0;i<16;++i){
      ind1[i]=0;
      ind2[i]=0;
    }
    somme1(0,min(k,n/2)-1);
    tab2[0][ind2[0]++]= 0;
 
    for (int i=k; i<n/2; ++i){
      res+= aux1(i, tab[i]);
      for (int j=i;j>0;--j)
	for (int l=0;l<ind1[j-1];++l)
	  tab1[j][ind1[j]++]= tab1[j-1][l]+tab[i];
    }

    for(int i=0;i<n/2;++i)
      sort(tab1[i], tab1[i]+ind1[i]);

    for (int i=n/2; i<n; ++i){
      res+= aux2(i, tab[i]);
      for (int j=i;j>0;--j)
	for (int l=0;l<ind2[j-1];++l)
	  tab2[j][ind2[j]++]= tab2[j-1][l]+tab[i];
    }
    cout << "Case " << cas << ": " << res << '\n';
  }
}
