 #include <iostream>
using namespace std;

#define DEBUG 1

#define EMPTY 0
#define BUMPER 1

// position 0 0 en bas à gauche
// x horizontaux
// y verticaux

#define RIGHT 0 // x croissants
#define UP 1    // y croissants
#define LEFT 2  // x decroissants
#define DOWN 3  // y decroissants

#define MAX 51

struct cellule {
  int type,value,cost;
  cellule(int t, int v, int c) : type(t), value(v), cost(c) {}
  cellule() : type(EMPTY), value(0), cost(0) {}
};

cellule t[MAX][MAX];
int sum;

int main() {
  sum = 0;
  int m,n,cw,p,v,c,x,y,d,l,score;
  cin >> m >> n >> cw >> p;
  for (int i=0; i<p; ++i) {
    cin >> x >> y >> v >> c;
    --x;--y;
    t[x][y] = cellule(BUMPER,v,c);
  }
  while (cin >> x >> y >> d >> l) {
    score = 0;
    --x;--y;
    while (l>1) {
      --l;
      if (d == UP) {
        if (y+1 == n-1) {
          l -= cw;
          d = RIGHT;
        }
        else if(t[x][y+1].type == BUMPER){
          score += t[x][y+1].value;
          l -= t[x][y+1].cost;
          d = RIGHT;
        }
        else ++y;
      }
      else if (d == RIGHT) {
        if (x+1 == n-1) {
          l -= cw;
          d = DOWN;
        }
        else if(t[x+1][y].type == BUMPER){
          score += t[x+1][y].value;
          l -= t[x+1][y].cost;
          d = DOWN;
        }
        else ++x;
      }    
      else if (d == DOWN) {
        if (y-1 == 0) {
            d = LEFT;
            l -= cw;
        }
        else if(t[x][y-1].type == BUMPER){
          score += t[x][y-1].value;
          l -= t[x][y-1].cost;
          d = LEFT;
        }
        else --y;
      }
      else if (d == LEFT) {
        if (x-1 == 0) {
          d = UP;
          l -= cw;
        }
        else if(t[x-1][y].type == BUMPER){
          score += t[x-1][y].value;
          l -= t[x-1][y].cost;
          d = UP;
        }
        else --x;
      }
      /*
      if (d == DOWN) {
        if (t[x][y].type == BUMPER) {
          l -= t[x][y].cost;
          if (l>0) score += t[x][y].value;
          if (x == 0) {
            d = UP;
            ++y;
          }
          else {
            d = LEFT;
            --x;
          }
          ++y;
        }
      }
      */
      //      cout << x << ' ' << y << " score " << score << " Life :" << l << " direction : " << d << endl;
    }
    //cout << "Fin de depl\n";
    cout << score << endl;
    sum += score;
  }
  cout << sum << endl;
  

  return 0;
}
