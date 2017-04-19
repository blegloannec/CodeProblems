#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef double fp;
typedef vector< vector<fp> > out_table;
typedef vector<fp> io_table;

// constantes
const fp eta = 0.5;
const int nb_in = 8;
const int nb_out = 8;
const int nb_hidden_layers = 1; // only 1 :-)
const int hidden_layer_size = 12;
const int training_iterations = 300;

// variables
int nb_tests, nb_examples, nb_layers;
vector<int> layer_size;
vector<io_table> tests, examples_in, examples_out;
vector< vector<fp> > Wtheta;
vector< vector< vector<fp> > > W;

fp rand_fp() {
  return (fp)rand()/RAND_MAX;
}

out_table Evaluate(const io_table &I) {
  out_table O(nb_layers);
  O[0] = I;
  for (int i=1; i<nb_layers; ++i)
    for (int u=0; u<layer_size[i]; ++u) {
      O[i].push_back(Wtheta[i][u]);
      for (int v=0; v<layer_size[i-1]; ++v)
	O[i][u] += O[i-1][v]*W[i-1][v][u];
      O[i][u] = 1 / (1 + exp(-O[i][u]));
    }
  return O;
}

void Backpropagation(const out_table &O, const io_table &T) {
  out_table Delta(nb_layers);
  for (int u=0; u<nb_out; ++u) // output nodes
    Delta[nb_layers-1].push_back(O[nb_layers-1][u]*(1-O[nb_layers-1][u])*(O[nb_layers-1][u]-T[u]));
  for (int i=nb_layers-2; i>0; --i) // hidden nodes
    for (int u=0; u<layer_size[i]; ++u) {
      Delta[i].push_back(0);
      for (int v=0; v<layer_size[i+1]; ++v) 
	Delta[i][u] += Delta[i+1][v]*W[i][u][v];
      Delta[i][u] *= O[i][u]*(1-O[i][u]);
    }
  for (int i=1; i<nb_layers; ++i)
    for (int v=0; v<layer_size[i]; ++v) {
      for (int u=0; u<layer_size[i-1]; ++u)
	W[i-1][u][v] -= eta*Delta[i][v]*O[i-1][u];
      Wtheta[i][v] -= eta*Delta[i][v];
    }
}

void Training() {
  for (int i=0; i<training_iterations; ++i)
    for (int j=0; j<nb_examples; ++j)
      Backpropagation(Evaluate(examples_in[j]),examples_out[j]);
}

io_table parseIO(string s) {
  io_table res;
  for (int i=0; i<(int)s.size(); ++i)
    res.push_back(s[i]=='0' ? 0. : 1.);
  return res;
}

int main() {
  srand(42);
  cin >> nb_tests >> nb_examples;
  nb_layers = nb_hidden_layers+2;
  layer_size.resize(nb_layers,hidden_layer_size);
  layer_size[0] = nb_in;
  layer_size[nb_layers-1] = nb_out;
  Wtheta.resize(nb_layers);
  for (int i=1; i<nb_layers; ++i)
    for (int u=0; u<layer_size[i]; ++u)
      Wtheta[i].push_back(rand_fp());
  W.resize(nb_layers-1);
  for (int i=0; i<nb_layers-1; ++i)
    for (int u=0; u<layer_size[i]; ++u) {
      vector<fp> V;
      for (int v=0; v<layer_size[i+1]; ++v)
	V.push_back(rand_fp());
      W[i].push_back(V);
    }
  for (int i=0; i<nb_tests; ++i) {
    string s;
    cin >> s;
    tests.push_back(parseIO(s));
  }
  for (int i=0; i<nb_examples; ++i) {
    string si,so;
    cin >> si >> so;
    examples_in.push_back(parseIO(si));
    examples_out.push_back(parseIO(so));
  }
  Training();
  for (int i=0; i<nb_tests; ++i) {
    out_table O = Evaluate(tests[i]);
    for (int j=0; j<nb_out; ++j)
      cout << (int)(O[nb_layers-1][j]+0.5);
    cout << endl;
  }
  return 0;
}
