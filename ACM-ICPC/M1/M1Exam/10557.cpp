#include <iostream>
#include <vector>
using namespace std;

#define MAX 101
#define INTMAX 100000

int size;
bool t[MAX][MAX]; // Table
int poids[MAX];
bool valide[MAX]; // etats accessibles
bool covalide[MAX]; // etats coaccessibles
int pred[MAX]; /* tableau des predecesseurs
		  A INITIALISER A -1 */

void clear_pred(int start) { // avant un DFS
  for (int i=0; i<size; ++i) pred[i] = -1;
  pred[start] = start;
}

void clear2() {
  for (int i=0; i<size; ++i) {
    valide[i] = false;
    covalide[i] = false;
    for (int j=0; j<size; ++j)
      t[i][j] = false;
  }
}

int dist[MAX];

// INITIALISER clear_pred(start);
void DFS(int start) {
  for (int i=0; i<size; ++i)
    if ((t[start][i]>0)&&(pred[i]<0)) {
      pred[i] = start;
      valide[i] = true;
      DFS(i);
    }
}

void DFS_inv(int start) {
  for (int i=0; i<size; ++i)
    if ((t[i][start])&&(pred[i]<0)) {
      pred[i] = start;
      covalide[i] = true; 
      DFS_inv(i);
    }
}

void relacher(int u, int v, int w) {
  int d2 = dist[u]+w;
  // on vérifie que d2<100 pour ne pas dépasser l'énergie.
  if (dist[v]>d2 && d2<100) {
    dist[v] = d2;
    pred[v] = u;
  }
}

bool bellman_ford(int start) { 
  // detecte les cycles de poids negatif
  for (int v=0; v<size; v++) { // initialisation
    dist[v] = INTMAX;
    pred[v] = -1;
  }
  dist[start] = 0;
  for (int j=1; j<size; j++) // relachements
    for (int u=0; u<size; u++) {
      if (valide[u] && covalide[u])
	for (int v=0; v<size; ++v)
	  if (valide[v] && covalide[v])
	    if (t[u][v]) relacher(u,v,poids[v]); // SIP
    }
  // detection des cycles negatifs, RINN
  for (int u=0; u<size; u++) 
    if (valide[u] && covalide[u])
      for (int v=0; v<size; ++v) 
	if (valide[v] && covalide[v])
	  if ((t[u][v])&&(dist[v]>dist[u]+poids[v])
	      // on vérifie que le sommet est bien accessible avec l'énergie
	      && dist[v]<INTMAX/2)
	    return false;
  return true;  
}


int main() {
  int k,d;
  while (cin >> size) {
    if (size < 0) return 0;
    clear2();
    for (int i=0; i<size; ++i) {
      cin >> poids[i] >> k;
      poids[i] = -poids[i];
      for (int j=0; j<k; ++j) {
	cin >> d;
	--d;
	t[i][d] = true;
      }
    }
    valide[0] = true;
    clear_pred(0);
    DFS(0);
    covalide[size-1] = true;
    clear_pred(size-1);
    DFS_inv(size-1);
    if (!bellman_ford(0)) 
      cout << "winnable\n";
    else if (dist[size-1]<100) 
      cout << "winnable\n";
    else 
      cout << "hopeless\n";
  }
  return 0;
}
