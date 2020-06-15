#ifndef _GRAPH_H
#define _GRAPH_H

#include <vector>
#include <climits>
using namespace std;  // very bad! but ok-ish here...

typedef long long weight;

typedef pair<int,weight> edge;
#define _v_ first
#define _w_ second
#define MAX_WEIGHT LLONG_MAX
const weight INF = MAX_WEIGHT;

typedef vector< vector<edge> > graph;

#endif
