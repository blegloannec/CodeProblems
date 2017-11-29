// E. The Amazing Triangle Counting Machine 

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct point {
  point(int a_x, int a_y): x(a_x), y(a_y) {}
  bool operator <(const point &op) const {return x < op.x || (x == op.x && y < op.y);}
//   void print() {cout << "(" << x << ", " << y << ")";}
  int x, y;
};

int hash(int x, int y)
{
  return ((x % 277)*256 + y) % 277;
}

vector< vector< int > > ht;
vector< pair< point, vector< point > > > g;

int find(int x, int y)
{
  int h, r=-1;

  h = hash(x, y);
  for (vector<int>::iterator it = ht[h].begin(); it != ht[h].end(); ++it)
    if (g[*it].first.x == x && g[*it].first.y == y)
      r = *it;

  return r;
}

void add(int x, int y, int i)
{
  int h = hash(x, y);

  ht[h].push_back(i);
}

int main(int argc, char *argv[])
{
  int nb_figs, nb_segs;
  double dx1, dy1, dx2, dy2;
  int x1, y1, x2, y2;
  int pos;
  int nb_triangles;

  ht.resize(277);

  cin >> nb_figs;

  for (int i = 0; i < nb_figs; ++i) {
    cin >> nb_segs;
    for (int j = 0; j < nb_segs; ++j) {
      cin >> dx1 >> dy1 >> dx2 >> dy2;
      x1 = dx1*10;
      y1 = dy1*10;
      x2 = dx2*10;
      y2 = dy2*10;

      pos = find(x1, y1);
      if (pos >= 0)
        g[pos].second.push_back(point(x2, y2));
      else {
        add(x1, y1, g.size());
        g.push_back(pair<point, vector<point> >(point(x1, y1),
                                                vector<point>(1, point(x2, y2))));
      }
          
      pos = find(x2, y2);
      if (pos >= 0)
        g[pos].second.push_back(point(x1, y1));
      else {
        add(x2, y2, g.size());
        g.push_back(pair<point, vector<point> >(point(x2, y2),
                                                vector<point>(1, point(x1, y1))));
      }
    }

    for (int j = 0; j < (int)g.size(); ++j)
      sort(g[j].second.begin(), g[j].second.end());

//     // affichage de g
//     for (int j = 0; j < (int)g.size(); ++j) {
//       g[j].first.print(); cout << " : ";
//       for (int k = 0; k < (int)g[j].second.size(); ++k) {
//         g[j].second[k].print(); cout << ", ";
//       }
//       cout << '\n';
//     }
//     cout << '\n';

    nb_triangles = 0;
    for (int j = 0; j < (int)g.size(); ++j)
      for (int k = 0; k < (int)g[j].second.size(); ++k)
        if (g[j].first < g[j].second[k]) {
          int l = 0, m = 0;
          pos = find(g[j].second[k].x, g[j].second[k].y);
//           cout << "considering: ";
//           g[j].first.print();
//           cout << " - ";
//           g[pos].first.print();
//           cout << '\n';
          while (l < (int) g[j].second.size() && m < (int)g[pos].second.size()) {
//             cout << "l = " << l << ",  m = " << m << '\n';
            if (g[j].second[l] < g[pos].second[m]) {
              ++l;
            } else if (g[pos].second[m] < g[j].second[l]) {
              ++m;
            } else {
              ++nb_triangles;
              ++l;
              ++m;
            }
          }
        }

    cout << (nb_triangles/3) << '\n';

    for (int j = 0; j < 277; ++j)
      ht[j].clear();
    g.clear();
  }  

  return 0;
}
