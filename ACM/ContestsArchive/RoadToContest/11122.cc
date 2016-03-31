#include <iostream>

using namespace std;

struct point
{
  long long x, y;
};

// det(p1, p2, p3) > 0 ssi (p1p2, p1p3) > 0
inline long long det(point &p1, point &p2, point &p3)
{
  return (p2.x-p1.x)*(p3.y-p1.y) - (p2.y-p1.y)*(p3.x-p1.x);
}

// in (p, p1, p2, p3) = true ssi p est dans le triangle p1,p2,p3 de manière large
inline bool in(point &p, point &p1, point &p2, point &p3)
{
  // si on a
  //     p3
  // p1
  //     p2
  if (det(p1, p2, p3) > 0)
    return det(p1, p2, p) >= 0 && det(p2, p3, p) >= 0 && det(p3, p1, p) >= 0;

    // autre cas
    //     p2
    // p1
    //     p3
  else if (det(p1, p2, p3) < 0)
    return det(p1, p3, p) >= 0 && det(p3, p2, p) >= 0 && det(p2, p1, p) >= 0;
  else return false;
}

// inter(p1, p2, p3, p4) = true ssi [p1, p2] et [p3, p4] s'intersectent strictement
inline bool inter(point &p1, point &p2, point &p3, point &p4)
{
  return det(p1, p3, p2)*det(p1, p2, p4) > 0
    && det(p3, p2, p4)*det(p3, p4, p1) > 0;
}

int main(int argc, char *argv[])
{
  int t;
  bool intersecte;
  point p[2][3];

  cin >> t;

  for (int i = 1; i <= t; ++i) {
    for (int j = 0; j < 2; ++j)
      for (int k = 0; k < 3; ++k)
	cin >> p[j][k].x >> p[j][k].y;

    intersecte = (det(p[0][0],p[0][1],p[0][2])!=0)&&(det(p[1][0],p[1][1],p[1][2])!=0);

    intersecte = intersecte && (
      in(p[0][0], p[1][0], p[1][1], p[1][2])
      && in(p[0][1], p[1][0], p[1][1], p[1][2])
      && in(p[0][2], p[1][0], p[1][1], p[1][2]));

    intersecte = intersecte || (
      in(p[1][0], p[0][0], p[0][1], p[0][2])
      && in(p[1][1], p[0][0], p[0][1], p[0][2])
      && in(p[1][2], p[0][0], p[0][1], p[0][2]));

    for (int j = 0; j < 3; ++j)
      for (int k = 0; k < 3; ++k)
	intersecte = intersecte || inter(p[0][j], p[0][(j+1)%3], p[1][k], p[1][(k+1)%3]);

    cout << "pair " << i << ": " << (intersecte ? "yes" : "no") << "\n";
  }

  return 0;
}
