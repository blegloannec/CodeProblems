//produit un couplage stable qui en plus est optimal pour les hommes
#define MAX 1000

int men[MAX][MAX]; //men[i][j] note de l'homme i pour la femme j
int women[MAX][MAX+1]; //idem

int mari[MAX]; //mari[i] indique le mari de la ieme femme
int femme[MAX]; //idem

void mariage(int n){    
  int k=0,X,x;
  for (int i=0;i<n;i++){
    mari[i]=n;
    women[i][n]=-1;
  }
  while (k<n){
    X=k;
    while (X!=n){
      int maxi=-1;
      for (int i=0;i<n;i++)
	if (men[X][i]>maxi){
	  x=i;
	  maxi=men[X][i];
	}
      
      if (women[x][X]>women[x][mari[x]]){
	int tmp=X;
	X=mari[x];
	mari[x]=tmp;
      }
      if (X!=n)
	men[X][x]=-1;
    }
    k++;
  }
  for (int i=0;i<n;i++)
    femme[mari[i]]=i;
}
