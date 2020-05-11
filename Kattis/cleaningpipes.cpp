/*
  If we build the intersection graph (where the vertices are the pipes and
  the edges indicate intersections), then the problem is solvable iff it
  is bipartite (hence there exists a set of vertices that is independent
  and covers all the edges).
  This leads to a O(P^2) solution, that relies on the intersection testing.
  To test whether two segments intersect, it is enough to observe that if
  it is not the case and that the segments are not //, then at least one
  of the segments has both ends strictly on one side of the line defined
  by the other.
  The reason is that both lines defined by the segments have to intersect
  in exactly one point. The segments intersect iff this point is inside both
  segments. Otherwise, there exists at least one segment not containing the
  intersection point. Then, such segment has to be fully on one side
  of the other segment.
*/
#include <iostream>
#include <vector>
using namespace std;
using ent = long long;

struct point {
  ent x,y;
  point(ent x, ent y) : x(x), y(y) {}
  point operator-(const point &A) const {
    return point(x-A.x, y-A.y);
  }
  ent operator*(const point &A) const {
    return x*A.y - y*A.x;
  }
  bool operator==(const point &A) const {
    return x==A.x && y==A.y;
  }
};

typedef vector< vector<int> > graph;

int W,P;
vector<int> Pstart;
vector<point> Well, Pdest;
vector< vector<int> > G;

int sign(ent x) {
  if (x==0) return 0;
  return x>0 ? 1 : -1;
}

bool intersect(int p1, int p2) {
  if (Pstart[p1]==Pstart[p2]) return false;
  point A1 = Well[Pstart[p1]], B1 = Pdest[p1];
  point A2 = Well[Pstart[p2]], B2 = Pdest[p2];
  if (B1==B2) return true;
  point V1 = B1-A1, V2 = B2-A2;
  // /!\ the following corner case is ok in this problem only
  //     in general we could have A1----B2--B1----A2
  //     but here this has to be  A1-----B1&2-----A2
  if (V1*V2==0) return false; // // or aligned
  // general case: testing sides
  return (sign(V1*(A2-A1))!=sign(V1*(B2-A1)) &&
	  sign(V2*(A1-A2))!=sign(V2*(B1-A2)));
}

bool bipartite(const graph &G) {
  int N = G.size();
  vector<int> color(N,0);
  for (int u0=0; u0<N; ++u0)
    if (color[u0]==0) {
      color[u0] = 1;
      vector<int> S;
      S.push_back(u0);
      while (!S.empty()) { // DFS
	int u = S.back();
	S.pop_back();
	for (int v : G[u]) {
	  if (color[v]==0) {
	    color[v] = 3 - color[u];
	    S.push_back(v);
	  }
	  else if (color[v]==color[u])
	    return false;
	}
      }
    }
  return true;
}

int main() {
  cin >> W >> P;
  for (int i=0; i<W; ++i) {
    int x,y;
    cin >> x >> y;
    Well.push_back(point(x,y));
  }
  Pstart.resize(P);
  for (int i=0; i<P; ++i) {
    int x,y;
    cin >> Pstart[i] >> x >> y;
    --Pstart[i];
    Pdest.push_back(point(x,y));
  }
  graph G(P);
  for (int p1=0; p1<P; ++p1)
    for (int p2=p1+1; p2<P; ++p2)
      if (intersect(p1,p2)) {
	G[p1].push_back(p2);
	G[p2].push_back(p1);
      }
  cout << (bipartite(G) ? "" : "im") << "possible\n";
  return 0;
}
