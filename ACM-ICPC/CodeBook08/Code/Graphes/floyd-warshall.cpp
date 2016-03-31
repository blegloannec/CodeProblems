int dist[MAX][MAX]; // distances, cf initialisation
int pred[MAX][MAX]; /* tableau des predecesseurs
		       pred[i][j] = sommet precedant j dans 
		       un plus court chemin de i a j */
void FloydWarshall() {
  // initialisation
  for (int i=0; i<size; ++i)
    for (int j=0; j<size; ++j) // WARNING. cas i=j
      if (t[i][j]>0) {
	dist[i][j] = w[i][j];
	pred[i][j] = i; // RINN
      }
      else {
	dist[i][j] = INTMAX;
	pred[i][j] = -1; // RINN
      }
  // prog. dyn.
  for (int k=0; k<size; ++k)
    // dist_k[i][j] = plus courte distance de i a j en utilisant les k premiers sommets
    for (int i=0; i<size; ++i)
      for (int j=0; j<size; ++j) {
	int d = dist[i][k]+dist[k][j];
	if (dist[i][j]>d) {
	  dist[i][j] = d;
	  pred[i][j] = pred[k][j]; // RINN
	}
      }
}
