#include <iostream>
using namespace std;

/* 
   Symmetries: geometrical, n-x on each cell (n the maximum digit)
   let A(s) = the nb of grids with sum s, A(s) = A(4n-s)
   Let S be the sum on each line/column/diagonal
   let X be the sum of the 4 corner elements
   let C be the sum of the 4 central elements
   let E be the sum of the 8 other (edges) elements
   then we have E = full square - both diagonals = 4S - 2S = 2S
   2C = 2 central lines + 2 central columns - E = 2S + 2S - 2S = 2S
   hence C = S
   X = both diagonals - C = 2S - S = S too
*/

int G[16];

int backtrack(int n, int s=0, int i=0) {
  int res = 0;
  switch (i) {
  case 3: {
    int s0 = G[0]+G[1]+G[2];
    for (int d=0; d<=n && s0+d<=2*n; ++d) {
      G[i] = d;
      int v = backtrack(n,s0+d,i+1);
      res += s0+d<2*n?2*v:v;
    }
    break;
  }
  case 7: {
    int d = s-G[4]-G[5]-G[6];
    if (0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 10: {
    int d = s-G[5]-G[6]-G[9];
    if (0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 11: {
    int d = s-G[8]-G[9]-G[10];
    if (0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 12: {
    int d = s-G[0]-G[4]-G[8];
    int e = s-G[3]-G[6]-G[9];
    if (d==e && 0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 13: {
    int d = s-G[1]-G[5]-G[9];
    if (0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 14: {
    int d = s-G[2]-G[6]-G[10];
    if (0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 15: {
    int d = s-G[12]-G[13]-G[14];
    int e = s-G[3]-G[7]-G[11];
    int f = s-G[0]-G[5]-G[10];
    if (d==e && d==f && 0<=d && d<=n) {
      G[i] = d;
      res = backtrack(n,s,i+1);
    }
    break;
  }
  case 16: {
    res = 1;
    break;
  }
  default: {
    for (int d=0; d<=n; ++d) {
      G[i] = d;
      res += backtrack(n,s,i+1);
    }
  }
  }
  return res;
}

int main() {
  int n;
  cin >> n;
  cout << backtrack(n) << endl;
  return 0;
}
