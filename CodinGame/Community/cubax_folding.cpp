#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
  On peut fixer arbitrairement les 2 premieres directions et
  obtenir les autres solutions par symetrie.
  Cela reduit l'espace de recherche d'un facteur 6 exactement.
*/

typedef unsigned long long ent;

struct vec {
  int x,y,z;
  vec(int x, int y, int z) : x(x), y(y), z(z) {}
};

const vector<char> D = {'U','D','R','L','F','B'};
const vector<vec> V = {vec(0,1,0),vec(0,-1,0),vec(1,0,0),vec(-1,0,0),vec(0,0,1),vec(0,0,-1)};

int N;
vector<int> B;
vector<unsigned int> S;
vector<string> Sol;
ent bfinal;

inline ent b(int x, int y, int z) {
  return 1LL<<((z<<4)|(y<<2)|x);
}

ent flip(int x, int y, int z, ent C, const vec &v, int l) {
  if (0<=x+l*v.x && x+l*v.x<N && 0<=y+l*v.y && y+l*v.y<N && 0<=z+l*v.z && z+l*v.z<N) {
    for (int k=1; k<=l; ++k) {
      ent bit = b(x+k*v.x,y+k*v.y,z+k*v.z);
      if (C&bit) return 0;
      C |= bit;
    }
    return C;
  }
  return 0;
}

string s2s(int r=0, bool inv = false) { // 0<=r<=2 la rotation
  string s;
  for (unsigned int i=0; i<S.size(); ++i) {
    int d = 0;
    if (inv && S[i]>1) {
      if (S[i]<4) d = 2;
      else d = -2;
    }
    s += D[(S[i]+d+2*r)%6];
  }
  return s;
}

void backtrack(int x=0, int y=0, int z=0, ent C=1, unsigned int i=0) {
  if (i==B.size()) {
    if (x==y && y==z && z==N-1) {
      Sol.push_back(s2s());
      // on ajoute les 5 solutions symetriques
      Sol.push_back(s2s(0,true));
      Sol.push_back(s2s(1));
      Sol.push_back(s2s(1,true));
      Sol.push_back(s2s(2));
      Sol.push_back(s2s(2,true));
    }
    return;
  }
  else if (C&bfinal) return;
  for (unsigned int d=0; d<6; ++d)
    //if (i==0 || S[S.size()-1]>>1!=d>>1) {
    if (S[S.size()-1]>>1!=d>>1) {
      ent NC = flip(x,y,z,C,V[d],B[i]);
      if (NC) {
	S.push_back(d);
	backtrack(x+B[i]*V[d].x,y+B[i]*V[d].y,z+B[i]*V[d].z,NC,i+1);
	S.pop_back();
      }
    }
}

int main() {
  cin >> N;
  bfinal = b(N-1,N-1,N-1);
  string SB;
  cin >> SB;
  for (unsigned int i=0; i<SB.size(); ++i)
    B.push_back((int)SB[i]-(int)'0'-1);
  // on commence par UR
  ent C0 = flip(0,0,0,1,V[0],B[0]);
  int x = B[0]*V[0].x, y = B[0]*V[0].y, z = B[0]*V[0].z;
  S.push_back(0);
  C0 = flip(x,y,z,C0,V[2],B[1]);
  x += B[1]*V[2].x;
  y += B[1]*V[2].y;
  z += B[1]*V[2].z;
  S.push_back(2);
  backtrack(x,y,z,C0,2);
  sort(Sol.begin(),Sol.end());
  for (unsigned int i=0; i<Sol.size(); ++i)
    cout << Sol[i] << endl;
  return 0;
}
