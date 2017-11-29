// ACM 260
#include <cstdio>
using namespace std;

const int MAX = 200;
int N;
bool B[MAX][MAX];
bool seen[MAX][MAX];

bool dfs(int i, int j) {
  if (j==N-1) return true;
  seen[i][j] = true;
  for (int di=-1; di<=1; ++di)
    if (0<=i+di && i+di<N)
      for (int dj=-1; dj<=1; ++dj)
	if (di+dj!=0 && 0<=j+dj && j+dj<N && B[i+di][j+dj] && !seen[i+di][j+dj])
	  if (dfs(i+di,j+dj)) return true;
  return false;
}

bool white_win() {
  for (int i=0; i<N; ++i)
    if (B[i][0] && !seen[i][0] && dfs(i,0)) return true;
  return false;
}

int main() {
  int cas = 1;
  while (true) {
    scanf("%d",&N);
    if (N==0) break;
    for (int i=0; i<N; ++i)
      for (int j=0; j<N; ++j) {
	char c;	
	scanf(" %c",&c);
	B[i][j] = (c=='w');
	seen[i][j] = false;
      }
    printf("%d %c\n", cas++, (white_win() ? 'W' : 'B'));
  }
  return 0;
}
