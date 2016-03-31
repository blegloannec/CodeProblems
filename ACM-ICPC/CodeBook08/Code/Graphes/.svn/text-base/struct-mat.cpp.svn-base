#include <queue>
#define MAX 500
int t[MAX][MAX]; // tableau du graphe
int s[MAX][MAX]; // tableau des poids
int size; // taille du tableau : size x size
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */
void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
}
void clear2(int t[MAX][MAX]) {
  for (int i=0; i<size; ++i) 
    for (int j=0; j<size; ++j)
      t[i][j] = 0;
}
