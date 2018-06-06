#include <iostream>
#include "message.h"
#include "flagpoles.h"
using namespace std;

typedef long long ll;

int id,nodes;
ll flags,il,ir;
ll leftL,leftD,maxL,rightL,rightD;
bool full;

void local_computation() {
  if (ir-il<=1) {
    maxL = 1;
    return;
  }
  ll L = 2, D = GetHeight(il+1)-GetHeight(il);
  maxL = leftL = L; leftD = D;
  full = true;
  for (ll i=il+2; i<ir; ++i) {
    ll D1 = GetHeight(i)-GetHeight(i-1);
    if (D1==D) {
      ++L;
      if (L>maxL) {
	maxL = L;
	if (full) {
	  leftL = maxL; leftD = D;
	}
      }
    }
    else {
      full = false;
      L = 2;
      D = D1;
    }
  }
  rightL = L; rightD = D;
}

void recv_update() {
  Receive(id-1);
  ll prev_rightL = GetLL(id-1);
  ll prev_rightD = GetLL(id-1);
  ll prev_maxL = GetLL(id-1);
  if (prev_maxL>maxL) maxL = prev_maxL;
  ll D = GetHeight(il)-GetHeight(il-1);
  if (D==leftD) {
    if (prev_rightD==D) leftL += prev_rightL;
    else ++leftL;
    if (leftL>maxL) maxL = leftL;
    if (full) rightL = leftL;
  }
}

void send_data() {
  PutLL(id+1,rightL);
  PutLL(id+1,rightD);
  PutLL(id+1,maxL);
  Send(id+1);
}

int main() {
  // init
  id = MyNodeId();
  nodes = NumberOfNodes();
  flags = GetNumFlagpoles();
  if (flags<3*nodes) {
    nodes = 1;
    if (id>0) return 0;
  }
  ll w = flags%nodes==0 ? flags/nodes : flags/(nodes-1);
  il = id*w, ir = min((id+1)*w,flags);
  
  // local computation
  local_computation();
  
  // update data taking into account the previous node data
  if (id>0) recv_update();

  // send data to next node
  if (id<nodes-1) send_data();
  else cout << maxL << endl;
  
  return 0;
}
