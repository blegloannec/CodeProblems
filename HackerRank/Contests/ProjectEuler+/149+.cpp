#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class MaxSum {
public:
  int curr,M;

  MaxSum() {
    curr = 0;
    M = INT_MIN;
  }
  
  void push(int u) {
    curr = u + max(curr,0);
    M = max(M,curr);
  }
        
  int get() {return M;}
};
    
// double-ended variant
class DEMaxSum {
public:
  int u0,currL,currR,ML, MR,sumL,sumR,max0L,max0R;

  DEMaxSum() {
    u0 = currL = currR = sumL = 0, sumR = 0;
    ML = MR = max0L = max0R = INT_MIN;
  }

  DEMaxSum(int v0) {
    u0 = currL = currR = ML = MR = sumL = sumR = max0L = max0R = v0;
  }
  
  void push(int l, int r) {
    currL = l + max(currL,0);
    ML = max(ML,currL);
    currR = r + max(currR,0);
    MR = max(MR,currR);
    sumL += l;
    max0L = max(max0L,sumL);
    sumR += r;
    max0R = max(max0R,sumR);
  }
        
  int get() {
    return max(max(ML,MR),max0L+max0R-u0);
  }
};

int main() {
  int N,l,m;
  int f0,f1,f2,f3,f4,g0,g1,g2,g3,g4;
  cin >> N;
  cin >> l;
  vector<int> A(l);
  for (int i=0; i<l; ++i) cin >> A[i];
  cin >> f0 >> f1 >> f2 >> f3 >> f4;
  cin >> m;
  vector<int> B(m);
  for (int i=0; i<m; ++i) cin >> B[i];
  cin >> g0 >> g1 >> g2 >> g3 >> g4;
  vector< vector<int> > T(N,vector<int>(N,0));
  T[0/N][0%N] = A[f0]+B[g0];
  T[1/N][1%N] = A[f1]+B[g1];
  T[2/N][2%N] = A[f2]+B[g2];
  T[3/N][3%N] = A[f3]+B[g3];
  T[4/N][4%N] = A[f4]+B[g4];
  for (int i=5; i<N*N; ++i) {
    int s = (f0+f1+f2+f3+f4)%l;
    f0 = f1; f1 = f2; f2 = f3; f3 = f4; f4 = s;
    s = (g0+g1+g2+g3+g4)%m;
    g0 = g1; g1 = g2; g2 = g3; g3 = g4; g4 = s;
    T[i/N][i%N] = A[f4]+B[g4];
  }
  vector<MaxSum> Rows(N), Cols(N), DiagsR(N), DiagsL(N);
  vector<DEMaxSum> AntiDiags;
  int M0 = INT_MIN;
  for (int n=0; n<N; ++n) {
    if (n>0) AntiDiags.push_back(DEMaxSum());
    AntiDiags.push_back(DEMaxSum(T[n][n]));
    for (int i=0; i<=n; ++i) {
      if (i<n) {
	Rows[i].push(T[i][n]);
	Cols[i].push(T[n][i]);
      }
      else {
	for (int j=0; j<=n; ++j) {
	  Rows[i].push(T[i][j]);
	  Cols[i].push(T[j][i]);
	}
      }
      M0 = max(M0,max(Rows[i].get(),Cols[i].get()));
      DiagsR[i].push(T[n-i][n]);
      DiagsL[i].push(T[n][n-i]);
      M0 = max(M0,max(DiagsR[i].get(),DiagsL[i].get()));
      if (2*i-1>=n) {
	AntiDiags[2*i-1].push(T[n][2*i-1-n],T[2*i-1-n][n]);
	M0 = max(M0,AntiDiags[2*i-1].get());
      }
      if (i<n && 2*i>=n) {
	AntiDiags[2*i].push(T[n][2*i-n],T[2*i-n][n]);
	M0 = max(M0,AntiDiags[2*i].get());
      }
    }
    cout << M0 << endl;
  }
  return 0;
}
