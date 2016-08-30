#include <iostream>
#include <fst/fstlib.h>
using namespace std;
using namespace fst;

/* FSA-based solution: build a small finite automaton for each constraint
   and iteratively build the global solution automaton adding a constraint
   at a time and intersecting + determinizing + minimizing at each step
   (hoping the intermediary automata remain quite compact).
   In the end, the final automaton is a single 17-state chain as the solution
   is unique.
   
   Using OpenFST library, runs in 1 min 25 and uses only ~220MB of RAM
   NB: 0 must not be used as an arc label, hence labels are +1
   
   Compile with:
   $ g++ --std=c++11 185.cpp -lfst

   Draw ;) the answer (final automaton):
   $ fstdraw out.fst | dot -Tpdf > sol.pdf
*/

#define ORD(C) ((int)(C)-(int)'0')

//const int N = 5;
//const int K = 6;
const int N = 16;
const int K = 22;
//string C[K] = {"90342","70794","39458","34109","51545","12531"};
//int V[K] = {2,0,2,1,2,1};
string C[K] = {"5616185650518293","3847439647293047","5855462940810587","9742855507068353","4296849643607543","3174248439465858","4513559094146117","7890971548908067","8157356344118483","2615250744386899","8690095851526254","6375711915077050","6913859173121360","6442889055042768","2321386104303845","2326509471271448","5251583379644322","1748270476758276","4895722652190306","3041631117224635","1841236454324589","2659862637316867"};
int V[K] = {2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2};

/* Generate the (16+1)(v+1)-state automaton
   of a given constraint (C,v) */
void gen_constraint(StdVectorFst &ac, string C, int v) {
  int states[N+1][v+1];
  for (int i=0; i<=N; ++i)
    for (int j=0; j<=v; ++j)
      states[i][j] = ac.AddState();
  ac.SetStart(states[0][0]);
  for (int i=0; i<N; ++i)
    for (int j=0; j<=v; ++j)
      for (int a=0; a<10; ++a) {
	if (ORD(C[i])==a) {
	  if (j<v) ac.AddArc(states[i][j],StdArc(a+1,a+1,TropicalWeight::One(),states[i+1][j+1]));
	}
	else ac.AddArc(states[i][j],StdArc(a+1,a+1,TropicalWeight::One(),states[i+1][j]));
      }
  ac.SetFinal(states[N][v],TropicalWeight::One());
  Minimize(&ac);
  //ac.Write(C+".fst");
}

int main() {
  StdVectorFst I;
  gen_constraint(I,C[0],V[0]);
  for (int i=1; i<K; ++i) {
    StdVectorFst A,J;
    gen_constraint(A,C[i],V[i]);
    Intersect(I,A,&J);
    Determinize(J,&I);
    Minimize(&I);
  }
  I.Write("out.fst");
  return 0;
}
