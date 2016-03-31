#define MAX 500
#define NB 2 // nombre de tableaux

int pred[MAX][MAX][MAX]; /* tableau des predecesseurs
			    a chaque etape */
int dist[NB][MAX][MAX];

void ProgDynToutesPaires() {
  int d,dmin,kmin;
  for (int l=0; l<size-1; ++l)
    for (int i=0; i<size; ++i)
      for (int j=0; i<size; ++j) {
	dmin = dist[l%NB][i][k];
	kmin = -1; // Warn. -1 on repasse directement au niveau precedent
	for(int k=0; k<size; ++k) {
	  d = dist[l%NB][i][k] + w[k][j];
	  if (d<dmin) {
	    dmin = d;
	    kmin = k; // RINN
	  }	  
	}
	dist[(l+1)%NB][i][j] = dmin;
	pred[l+1][i][j] = kmin; // RINN
      }
}
