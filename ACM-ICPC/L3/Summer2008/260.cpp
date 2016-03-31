// ACM 260
#include <cstdio>

#define MAX 100

bool board[MAX][MAX];
bool visited[MAX][MAX];

bool white_win() {
  for 
  return false;
}

bool inboard(int i, int j) {
  
}

int main() {
  int t;
  char c;
  
  while (scanf("%d", &t)==1) {
    for (int i=0; i<t; i++)
      for (int j=0; j<t; j++) {
	scanf("%c",c);
	board[i][j] = (c=='W');
      }
  }
}
