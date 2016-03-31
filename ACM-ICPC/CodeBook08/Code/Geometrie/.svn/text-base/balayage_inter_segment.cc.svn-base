#include <iostream>
#include <queue>
#include <set>

using namespace std;

// Point (debut ou fin de segment)
// contient aussi les coordonnees de l'autre point pour tester l'intersection, ...
struct Point
{
  Point(double x, double y, double xe, double ye):
    m_x(x), m_y(y), m_xe(xe), m_ye(ye) {}

  double m_x, m_y, m_xe, m_ye;  // coordonnees du point et de l'autre extremite du segment

  // vrai ssi le point est une extremite gauche de segment
  bool est_gauche() const {return m_x < m_xe || m_x == m_xe && m_y < m_ye;}

  // retourne det ((x-m_x, y-m_y), (m_xe-m_x, m_ye-m_y))
  double det(double x, double y) const
  {
    return (x-m_x)*(m_ye-m_y)-(y-m_y)*(m_xe-m_x);
  }

  bool operator==(const Point &p) const
  {
    return m_x == p.m_x && m_y == p.m_y && m_xe == p.m_xe && m_ye == p.m_ye;
  }

  // ordre dans la structure de donnees set
  // (on est alors sur que est_gauche vaut true pour les deux points)
  bool operator<(const Point &p) const
  {
    double d;

    if (m_x < p.m_x || m_x == p.m_x && m_y < p.m_y)
      return !(p == *this || p < *this);

    if (m_x < p.m_xe) {
      d = p.det(m_x, m_y);
      if (d != 0) return d > 0;
      // this appartient a la droite definie par p
      // on essaye alors de comparer les pentes
      d = p.det(m_xe, m_ye);
      if (d != 0) return d > 0;
      // si c'est colineaire, on regarde qui commence en premier
      return m_x < p.m_x || m_x == p.m_x && m_y < p.m_y;
    } else  // m_x == p.m_xe car on compare ce qui est comparable
      return m_y < p.m_y || p.m_x < p.m_xe && m_y < p.m_ye;
  }

  // renvoie vrai ssi le segment commencant a this intersecte le segment comencant a p
  bool intersecte(const Point &p) const
  {
    return det(p.m_x, p.m_y)*det(p.m_xe, p.m_ye) <= 0
      && p.det(m_x, m_y)*p.det(m_xe, m_ye) <= 0;
  }

  // met dans (xi, yi) les coordonnees de l'intersection entre this et p
  void coord_inter(const Point &p, double *xi, double *yi) const
  {
    // on note a*x+b*y=c et ap*x+bp*y=cp les equations des deux droites
    double a = m_y-m_ye, b = m_xe-m_x;
    double c = a*m_x+b*m_y;
    double ap = p.m_y-p.m_ye, bp = p.m_xe-p.m_x;
    double cp = ap*p.m_x+bp*p.m_y;

    double det = a*bp-ap*b;

    if (det) {
      *xi = (c*bp-cp*b)/det;
      *yi = (a*cp-ap*c)/det;
    } else {
      // on suppose un nombre fini d'intersections
      // donc si les segments sont colineaires
      // c'est que l'intersection a lieu a une extremite
      *xi = (m_x == p.m_x || m_x == p.m_xe) ? m_x : m_xe;
      *yi = (m_y == p.m_y || m_y == p.m_ye) ? m_y : m_ye;
    }
  }
};

// ordre des evenements (sweeping line)
struct Ordre
{
  bool operator()(const Point &i,const Point &j) const
  {
    // la, j'aurais du commenter en l'ecrivant
    // parce que maintenant, je ne me souviens plus pourquoi c'est aussi complique
    // (en fait, c'est un tri lexicographique sur (x, 1-est_gauche, y) mais je sais
    // plus pourquoi on utilise est_gauche)
    return i.m_x > j.m_x ||
      i.m_x == j.m_x && (!(i.est_gauche()) && j.est_gauche() ||
			 i.est_gauche() == j.est_gauche() && i.m_y > j.m_y);
  }
};

// points des evenements (tas min)
priority_queue<Point, vector<Point>, Ordre> pq;

// structure de donnees contenant les segments intersectant
// la sweeping line (verticale) dans l'ordre de ces intersections
// (cf. Point::operator< pour les details)
set<Point> s;

// coupe le segment *it en (x, y) (typiquement point d'intersection avec un autre segment)
void coupure(set<Point>::iterator it, double x, double y)
{
  if ((it->m_x != x || it->m_y != y)
      && (it->m_xe != x || it->m_ye != y)) {

    s.insert(Point(it->m_x, it->m_y, x, y));
    pq.push(Point(x, y, it->m_x, it->m_y));  // fin de la partie avant l'intersection

    pq.push(Point(x, y, it->m_xe, it->m_ye));  // debut de la partie apres l'intersection
    pq.push(Point(it->m_xe, it->m_ye, x, y));  // fin de la partie apres l'intersection

    s.erase(it);
  }
}

int main(int argc, char *argv[])
{
  int n;  // nombre de segments
  double x1, y1, x2, y2;
  set<Point>::iterator it, itp, itn;

  // En tete postscript encapsule
  cout << "%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 100 100\n1.1 setlinewidth" << endl;

  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> x1 >> y1 >> x2 >> y2;
    pq.push(Point(x1, y1, x2, y2));
    pq.push(Point(x2, y2, x1, y1));
    // affichage des segments
    cout << x1 << ' ' << y1 << " moveto " << x2 << ' ' << y2 << " lineto stroke" << endl;
  }

  // on deplace la barre d'evenements (de la gauche vers la droite)
  while (!(pq.empty())) {
    if (pq.top().est_gauche()) {
      // si c'est un debut,
      // on insere dans la structure de donnees
      s.insert(pq.top());
      it = s.find(pq.top());

      // puis on teste l'intersection avec le precedent...
      itp = it;
      if (itp != s.begin() && it->intersecte(*(--itp))) {
	it->coord_inter(*itp, &x1, &y1);
	cout << x1 << ' ' << y1 << " 2 0 360 arc stroke" << endl;
	coupure(itp, x1, y1);
	coupure(it, x1, y1);
      }

      // ...et avec le suivant
      itn = it;
      if (++itn != s.end() && it->intersecte(*itn)) {
	it->coord_inter(*itn, &x1, &y1);
	cout << x1 << ' ' << y1 << " 2 0 360 arc stroke" << endl;
	coupure(it, x1, y1);
	coupure(itn, x1, y1);
      }
    } else {
      // sinon c'est une fin de segment
      // on enleve le segment de la structure de donnees s...
      it = s.find(Point(pq.top().m_xe, pq.top().m_ye, pq.top().m_x, pq.top().m_y));
      // comme on ne peut pas supprimer de la pq, on peut y avoir des fins de segments obsoletes
      if (it != s.end()) {

	// ... et on verifie que suivant et precedent ne s'intersectent pas
	itp = itn = it;
	if (itp != s.begin() && ++itn != s.end() && (--itp)->intersecte(*itn)) {
	  itp->coord_inter(*itn, &x1, &y1);
	  cout << x1 << ' ' << y1 << " 2 0 360 arc stroke" << endl;
	  coupure(itp, x1, y1);
	  coupure(itn, x1, y1);
	}
	
	s.erase(it);
      }
    }
    pq.pop();
  }

  return 0;
}
