#include <iostream>
using namespace std;

#define MAX 21

bool t[MAX][MAX];
int d[MAX];
int n;

bool contientK33() {
  for (int i1=1; i1<=n; i1++) {
    if (d[i1]>0) {
      for (int i2=i1+1; i2<=n; i2++) {
	if (d[i2]>0) {
	  for (int i3=i2+1; i3<=n; i3++) {
	    if (d[i3]>0) {
	      for (int i4=2; i4<=n; i4++) {
		if ((d[i4]>0)&&(i4!=i1)&&(i4!=i2)&&(i4!=i3)) {
		  for (int i5=i4+1; i5<=n; i5++) {
		    if ((d[i5]>0)&&(i5!=i1)&&(i5!=i2)&&(i5!=i3)) {
		      for (int i6=i5+1; i6<=n; i6++) {
			if ((d[i6]>0)&&(i6!=i1)&&(i6!=i2)&&(i6!=i3)) {
			  if ((t[i1][i4])&&(t[i1][i5])&&(t[i1][i6])&&
			      (t[i2][i4])&&(t[i2][i5])&&(t[i2][i6])&&
			      (t[i3][i4])&&(t[i3][i5])&&(t[i3][i6])) return true;
			  
			}
		      }
		    }
		  }
		}
	      }
	    }
	  }
	}
      }
    }
  }
  return false;
}

bool contientK5() {
  for (int i1=1; i1<=n; i1++) {
    if (d[i1]>3) {
      for (int i2=i1+1; i2<=n; i2++) {
	if (d[i2]>3) {
	  for (int i3=i2+1; i3<=n; i3++) {
	    if (d[i3]>3) {
	      for (int i4=i3+1; i4<=n; i4++) {
		if (d[i4]>3) {
		  for (int i5=i4+1; i5<=n; i5++) {
		    if (d[i5]>3) {
		      if ((t[i1][i2])&&(t[i1][i3])&&(t[i1][i4])&&(t[i1][i5])&&
			  (t[i2][i3])&&(t[i2][i4])&&(t[i2][i5])&&
			  (t[i3][i4])&&(t[i3][i5])&&
			  (t[i4][i5])) return true;
		      
		    }
		  }
		}
	      }
	    }
	  }
	}
      }
    }
  }
  return false;
}

int main() {
  int m,a,b;
  while (cin >> n >> m) {
    for (int i=1; i<=n; i++) {
      d[i]=0;
      for (int j=1; j<=n; j++) 
	t[i][j] = false;
    }
    for (int i=1; i<=m; i++) {
      cin >> a >> b;
      d[a]++;
      d[b]++;
      t[a][b] = t[b][a] = true;
    }
    bool test0,test;
    test0 = true;
    while (test0) {
      test0 = false;
      test = true;
      while (test) {
	test = false;
	for (int i=1; i<=n; i++) {
	  if (d[i]==1) {
	    test0 = test = true;
	    for (int j=1; j<=n; j++) {
	      if (t[i][j]) {
		t[i][j]=t[j][i]=false;
		d[j]--;
		d[i]=0;
		break;
	      }
	    }
	  }
	}
      }
      test = true;
      while(test) {
	test = false;
	for (int i=1; i<=n; i++) {
	  if (d[i]==2) {
	    test = test0 = true;
	    int a,b;
	    bool un = false;
	    for (int j=0; j<=n; j++) {
	      if (t[i][j]) {
		if (!un) {
		  a = j;
		  un = true;
		  t[i][j]=t[j][i]=false;
		}
		else {
		  b = j;
		  t[i][j]=t[j][i]=false;
		  break;
		}
	      }
	    }
	    if (t[a][b]) {
	      d[a]--;
	      d[b]--;
	    }
	    else {
	      t[a][b]=t[b][a]=true;
	    }
	    d[i] = 0;
	  }
	}
      }
    }
    if ((!contientK33())&&(!contientK5())) cout << "YES\n";
    else cout << "NO\n";      
  }
  return 0;
}
