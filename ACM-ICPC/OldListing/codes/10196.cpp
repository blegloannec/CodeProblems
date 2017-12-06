//10196

#include <iostream>
using namespace std;

char chess[12][12];
int blacki; // de 2 à 9
int blackj;
int whitei;
int whitej;
int cpt;



void efface(void){
  blacki = 0;
  blackj = 0;
  whitei = 0;
  whitej = 0;

  for(int i = 0; i < 12; ++i){
    for(int j = 0; j < 12; ++j){
      chess[i][j] = '.';
    }
  }
  return;
}

bool touch_black_p(int i_p, int j_p){//est-ce que le pion noir met en echec le roi blanc ?
  return ((whitei == i_p+1) && ((whitej == j_p +1) || (whitej == j_p-1)));
}
bool touch_white_p(int i_p, int j_p){//est-ce que le pion blanc met en echec le roi noir ?
  return ((blacki == i_p-1) && ((blackj == j_p +1) || (blackj == j_p-1)));
}


bool touch_black_n(int i_n, int j_n){
  return (
          ((whitei == i_n-2) && (whitej == j_n-1 || whitej == j_n+1)) ||
          ((whitei == i_n+2) && (whitej == j_n-1 || whitej == j_n+1)) ||

          ((whitei == i_n-1 || whitei == i_n+1) && (whitej == j_n+2)) ||
          ((whitei == i_n-1 || whitei == i_n+1) && (whitej == j_n-2)) 
         );
}
bool touch_white_n(int i_n, int j_n){
  return (
          ((blacki == i_n-2) && (blackj == j_n-1 || blackj == j_n+1)) ||
          ((blacki == i_n+2) && (blackj == j_n-1 || blackj == j_n+1)) ||

          ((blacki == i_n-1 || blacki == i_n+1) && (blackj == j_n+2)) ||
          ((blacki == i_n-1 || blacki == i_n+1) && (blackj == j_n-2)) 
         );
}

//faut tester les autres pieces
bool touch_black_b(int i_b, int j_b){
  int i1 = whitei-i_b;
  int j1 = whitej-j_b;
  if(abs(i1) == abs(j1)){
    bool occup = false;
    if(i1 > 0 && j1 > 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b+i][j_b+i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 > 0 && j1 < 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b+i][j_b-i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 < 0 && j1 > 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b-i][j_b+i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 < 0 && j1 < 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b-i][j_b-i] != '.'){
	  occup = true;
	}
      }
    }
    return !occup;
  }
  return false;
}
//faut tester les autres pieces
bool touch_white_b(int i_b, int j_b){
  int i1 = blacki-i_b;
  int j1 = blackj-j_b;
  if(abs(i1) == abs(j1)){
    bool occup = false;
    if(i1 > 0 && j1 > 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b+i][j_b+i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 > 0 && j1 < 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b+i][j_b-i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 < 0 && j1 > 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b-i][j_b+i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 < 0 && j1 < 0){
      for(int i = 1; i < abs(i1);++i){
	if(chess[i_b-i][j_b-i] != '.'){
	  occup = true;
	}
      }
    }
    return !occup;
  }
  return false;
}

bool touch_black_r(int i_r, int j_r){
  if(whitei == i_r || whitej == j_r){
    bool occup = false;
    int i1 = whitei-i_r;
    int j1 = whitej-j_r;
    if(i1 == 0 && j1 > 0){
      for(int i = 1; i < abs(j1); ++i){ 
	if(chess[i_r][j_r+i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 == 0 && j1 < 0){
      for(int i = 1; i < abs(j1); ++i){ 
	if(chess[i_r][j_r-i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 > 0 && j1 == 0){
      for(int i = 1; i < abs(i1); ++i){ 
	if(chess[i_r+i][j_r] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 < 0 && j1 == 0){
      for(int i = 1; i < abs(i1); ++i){ 
	if(chess[i_r-i][j_r] != '.'){
	  occup = true;
	}
      }
    }
    return !occup;
  }
  return false;
}

bool touch_white_r(int i_r, int j_r){
  if(blacki == i_r || blackj == j_r){
    bool occup = false;
    int i1 = blacki-i_r;
    int j1 = blackj-j_r;
    if(i1 == 0 && j1 > 0){
      for(int i = 1; i < abs(j1); ++i){ 
	if(chess[i_r][j_r+i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 == 0 && j1 < 0){
      for(int i = 1; i < abs(j1); ++i){ 
	if(chess[i_r][j_r-i] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 > 0 && j1 == 0){
      for(int i = 1; i < abs(i1); ++i){ 
	if(chess[i_r+i][j_r] != '.'){
	  occup = true;
	}
      }
    }
    if(i1 < 0 && j1 == 0){
      for(int i = 1; i < abs(i1); ++i){ 
	if(chess[i_r-i][j_r] != '.'){
	  occup = true;
	}
      }
    }
    return !occup;
  }
  return false;
}

bool touch_black_q(int i_q, int j_q){
  return touch_black_b(i_q, j_q)||touch_black_r(i_q, j_q);
}
bool touch_white_q(int i_q, int j_q){
  return touch_white_b(i_q, j_q)||touch_white_r(i_q, j_q);
}

void evalue(void){
  for(int i = 2; i < 10; ++i){
    for(int j = 2; j < 10; ++j){
      switch(chess[i][j]) {

      case 'P':
        {
          if(touch_white_p(i,j)){
            cout << "Game #" << cpt << ": black king is in check.";
            return;
          }
          break;
        }
      case 'N':
        {
          if(touch_white_n(i,j)){
            cout << "Game #" << cpt << ": black king is in check.";
            return;
          }
          break;
        }
      case 'B':
        {
          if(touch_white_b(i,j)){
            cout << "Game #" << cpt << ": black king is in check.";
            return;
          }
          break;
        }
      case 'R':
        {
          if(touch_white_r(i,j)){
            cout << "Game #" << cpt << ": black king is in check.";
            return;
          }
          break;
        }
      case 'Q':
        {
          if(touch_white_q(i,j)){
            cout << "Game #" << cpt << ": black king is in check.";
            return;
          }
          break;
        }

      case 'p':
        {
          if(touch_black_p(i,j)){
            cout << "Game #" << cpt << ": white king is in check.";
            return;
          }
          break;
        }
      case 'n':
        {
          if(touch_black_n(i,j)){
            cout << "Game #" << cpt << ": white king is in check.";
            return;
          }
          break;
        }
      case 'b':
        {
          if(touch_black_b(i,j)){
            cout << "Game #" << cpt << ": white king is in check.";
            return;
          }
          break;
        }
      case 'r':
        {
          if(touch_black_r(i,j)){
            cout << "Game #" << cpt << ": white king is in check.";
            return;
          }
          break;
        }
      case 'q':
        {
          if(touch_black_q(i,j)){
            cout << "Game #" << cpt << ": white king is in check.";
            return;
          }
          break;
        }

      };//fin switch
    };
  };
  
  cout << "Game #" << cpt << ": no king is in check.";
}

int main(void){
  cpt = 0;
  int vide;
  

  while(cpt != -1){
    efface(); //efface l'echiquier
    vide = 0;
    char stk[9];

    for(int i = 0; i < 8; ++i){
      cin >> stk; //met la ligen dans stk
      for(int j = 0; j < 8; ++j){ //recopie dans l'echiquier
        chess[2+i][2+j] = stk[j]; 
        if(stk[j] != '.'){
          vide = 1;
        }
        // repere les deux rois
        if(stk[j] == 'k'){
          blacki = i+2;
          blackj = j+2;
        }
        if (stk[j] == 'K'){
          whitei = i+2;
          whitej = j+2;
        }
      }
    }
    if (vide == 0){
      return 0;
    }
    
    //if(cpt > 0) {cout << endl;}
    cpt++;
    evalue();
    cout << endl;
    cin.ignore();
    
  } 
}
