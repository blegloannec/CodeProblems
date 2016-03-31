#include <vector>
#include <queue>
#define MAX 500
struct edge {
  int dest,weight;
  edge(int d, int w) : dest(d), weight(w) {};
};
typedef vector<edge> liste;
int size;
liste t[MAX]; // Table des listes de successeurs
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
}
