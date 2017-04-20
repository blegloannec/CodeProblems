#include <iostream>
#include <vector>
using namespace std;

/*
  Si l'on retire une arete de l'arbre, on obtient 2 arbres de diametres
  D1 et D2 et l'on est certain de pouvoir les connecter de facon
  a former un arbre de diametre D1+D2.

  Il s'agit donc de calculer pour chaque arete les diametres des sous-arbres
  de part et d'autre.
  Lors d'un calcul classique du diametre d'un arbre, on fait remonter, par un
  DFS depuis une racine arbitraire, pour chaque noeud rencontre, les diametres
  des sous-arbres enracines en chacun de ses fils ainsi que la longueur du
  plus long chemin se terminant en ce fils dans son sous-arbre.

  On a donc apres ca quasiment toute l'information necessaire pour chaque
  sommet : il ne manque de l'info pour le sous-arbre du cote de son pere
  lors du parcours. A l'exception de la racine pour laquelle on a tout.

  Il suffit donc de refaire un parcours depuis la racine en calculant au fur
  et a mesure et en faisant redescendre l'info manquante.
*/

int n;
vector< vector<int> > G;
vector<int> sub_diam;
vector<int> max_path;

// classic diameter computation
void diameter(int u=0, int u0=-1) {
  int mp1 = 0, mp2 = 0;
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      diameter(*iv,u);
      max_path[u] = max(max_path[u],max_path[*iv]+1);
      if (max_path[*iv]+1>mp1) {
	mp2 = mp1;
	mp1 = max_path[*iv]+1;
      }
      else if (max_path[*iv]+1>mp2)
	mp2 = max_path[*iv]+1;
      sub_diam[u] = max(sub_diam[u],sub_diam[*iv]);
    }
  sub_diam[u] = max(sub_diam[u],mp1+mp2);
}

/*
  second pass
  u0 ---> u ---> v
  (le sens des aretes est celui de la premiere passe)
  sd = subtree diameter, mp = max path from root
  sd1(u), mp1(u) les infos calculees en premiere passe
  l'info descendue (sd,mp) est celle du sous-arbre "gauche" enracine en u
  les infos du sous-arbre "droit" enracine en u sont connues via
  la premiere passe
  si l'on fixe v, pour passer de (u0,u) a (u,v)
  on doit calculer les info du sous-arbre gauche enracine en u0
  mp' = max(mp+1, max{mp1(v')+1 pour u -> v' =/= v})
  sd' = max(sd, max{sd1(v') pour v' =/= v'},
                max{mp+1+mp1(v') pour v' =/= v},
                max{mp1(v')+mp1(v'') pour v' /= v'' et v',v'' =/= v})
  pour un calcul en O(1) pour chaque v on a besoin de pre-calculer
  les 3 mp1(v) maximaux et les 2 sd1(v) maximaux
  NB : il est important de prendre mp = -1 a l'initialisation qui 
       part d'une arete u0 -> u1 fictive (u0 = -1 n'existe pas)
  NB2 : il est important dans le pre-calcul de prendre les mp1(v)+1 (de facon a
        avoir 0 dans les calculs quand la valeur n'existe pas, i.e. par exemple
	il n'y a que 2 fils mais on prend les 3 valeurs max donc si l'on +1
	a posteriori, alors on compte 1 pour une valeur n'existant pas,
	ou bien il faudrait initialiser a -1 mais cela peut a priori poser pb
	dans certains cas particuliers)
*/
int dfs(int u=0, int u0=-1, int sd=0, int mp=-1) {
  int mp1=0, mp2=0, mp3=0, sd1=0, sd2=0;
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      if (max_path[*iv]+1>mp1) {
	mp3 = mp2;
	mp2 = mp1;
	mp1 = max_path[*iv]+1;
      }
      else if (max_path[*iv]+1>mp2) {
	mp3 = mp2;
	mp2 = max_path[*iv]+1;
      }
      else if (max_path[*iv]+1>mp3)
	mp3 = max_path[*iv]+1;
      if (sub_diam[*iv]>sd1) {
	sd2 = sd1;
	sd1 = sub_diam[*iv];
      }
      else if (sub_diam[*iv]>sd2)
	sd2 = sub_diam[*iv];
    }
  int res = u0<0 ? sub_diam[u] : sd+1+sub_diam[u];
  for (vector<int>::iterator iv=G[u].begin(); iv!=G[u].end(); ++iv)
    if (*iv!=u0) {
      int mpv = max(mp+1,(mp1==max_path[*iv]+1 ? mp2 : mp1));
      int sdv = max(sd,(sd1==sub_diam[*iv] ? sd2 : sd1));
      sdv = max(sdv,mp+1+(mp1==max_path[*iv]+1 ? mp2 : mp1));
      if (max_path[*iv]+1==mp1) sdv = max(sdv,mp2+mp3);
      else if (max_path[*iv]+1==mp2) sdv = max(sdv,mp1+mp3);
      else sdv = max(sdv,mp1+mp2);
      res = max(res,dfs(*iv,u,sdv,mpv));
    }
  return res;
}

int main() {
  cin >> n;
  G.resize(n);
  sub_diam.resize(n,0);
  max_path.resize(n,0);
  for (int m=0; m<n-1; ++m) {
    int u,v;
    cin >> u >> v; --u; --v;
    G[u].push_back(v);
    G[v].push_back(u);
  }
  diameter();
  cout << dfs() << endl;
  return 0;
}
