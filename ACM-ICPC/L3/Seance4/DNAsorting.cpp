/*
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_N 50
#define MAX_M 100

int n,m;
vector<string> data(MAX_M);
int cal[MAX_N][4];


bool cmp(string i, string j){
  if (i=="")
    return false;
    else if (j=="")
      return true;
 
  else{ 
    int a,b,c,d;
    a= i[n]-48;
    b= i[n+1]-48;
    c= j[n]-48;
    d= j[n+1]-48;
    
    a=10*a+b;
    c=10*c+d;
    
    return (a<c);
  }
}

void aux(){
  if (n==0)
    for (int i=0; i<m-1; cout<<"\n",++i);
  else{
    for (int i=0; i<m; ++i){
      cin >> data[i];
      data[i].append(2, ' ');
      
      for (int k=0; k<n; ++k)
	cal[k][0]=cal[k][1]=cal[k][2]=cal[k][3]=0;
      if (data[i][n-1]=='A')
	cal[n-1][0] = 1;
      else if  (data[i][n-1]=='C')
	cal[n-1][1] = 1;
      else if  (data[i][n-1]=='G')
	cal[n-1][2] = 1;
      else
	cal[n-1][3] = 1;
      for (int j=(n-2); j>=0; --j){
	cal[j][0]= cal[j+1][0];
	cal[j][1]= cal[j+1][1];
	cal[j][2]= cal[j+1][2];
	cal[j][3]= cal[j+1][3];
	if (data[i][j]=='A')
	  cal[j][0] = cal[j][0]+1;
	else if  (data[i][j]=='C')
	  cal[j][1] = cal[j][1]+1;
	else if  (data[i][j]=='G')
	  cal[j][2] = cal[j][2]+1;
	else
	  cal[j][3] = cal[j][3]+1;
      }
      int nb_inverse=0;
      for (int j=0; j<n; ++j){
	// cout << cal[j][0] << " " << cal[j][1] << " " << cal[j][2] << " " << cal[j][3] << endl;
	
	if (data[i][j]=='A')
	  nb_inverse = nb_inverse;
	else if  (data[i][j]=='C')
	  nb_inverse = nb_inverse+ cal[j][0];
	else if  (data[i][j]=='G')
	  nb_inverse = nb_inverse+ cal[j][0]+ cal[j][1];
	else
	  nb_inverse = nb_inverse+ cal[j][0]+ cal[j][1]+ cal[j][2];
      }
      data[i][n]=(nb_inverse/10+ 48);
      data[i][n+1]=(nb_inverse%10+ 48);
      
      int a,b;
      a= data[i][n]-48;
      b= data[i][n+1]-48;
      
      a=10*a+b;
    }
  }
  
  stable_sort(data.begin(), data.end(), cmp);
  
  for (int i=0; i<m; ++i){
    data[i].erase(n);
    cout << data[i] << "\n";
  }
}

int main(){
  int nb_case;
  scanf("%d", &nb_case);
  
  for (int i=0; i<nb_case-1; i++){
    scanf("%d %d", &n, &m);
    aux();
    printf("\n");
  }
  scanf("%d %d", &n, &m);
  aux();
  cout << endl;
  
  return 0;
}*/


// DNA sorting

#include <iostream>
#include <string>
#include <list>
using namespace std;

/* Un majorant du nb d'inversions est 
   n(n-1)/2 pour un mot de taille n.
*/

#define MAX 1300

int n;
list<string> t[MAX];

int nb_inv(string &s) {
  int a,c,g,res;
  a = c = g = res = 0;
  string::reverse_iterator it;
  for (it=s.rbegin(); it!=s.rend(); it++) {
    if (*it=='A') ++a;
    else if (*it=='C') {
      ++c;
      res += a;
    }
    else if (*it=='G') {
      ++g;
      res += a+c;
    }
    else res += a+c+g;
  }
  // cout << s << ' ' << res << endl;
  return res;
}

int main() {
  string s;
  int M,m;
  cin >> M;
  
  while (M-->1) {
    for (int i=0; i<MAX; i++) t[i].clear();
    cin >> n >> m;
    for (int i=0; i<m; i++) { // tri linÃ©aire
      cin >> s;
      t[nb_inv(s)].push_back(s);
    }
    for (int i=0; i<MAX; i++) {
      while (!t[i].empty()) {
	cout << t[i].front() << '\n';
	t[i].pop_front();
      }
    }
    cout << '\n';
  }

  for (int i=0; i<MAX; i++) t[i].clear();
  cin >> n >> m;
  for (int i=0; i<m; i++) { // tri linÃ©aire
    cin >> s;
    t[nb_inv(s)].push_back(s);
  }
  for (int i=0; i<MAX; i++) {
    while (!t[i].empty()) {
      cout << t[i].front() << '\n';
	t[i].pop_front();
    }
  }
  

  return 0;
}
