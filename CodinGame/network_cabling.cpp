#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int N;
    cin >> N;
    int Xmin = INT_MAX, Xmax = INT_MIN;
    vector<int> Y(N);
    for (int i=0; i<N; ++i) {
        int x;
        cin >> x >> Y[i];
        Xmin = min(Xmin,x);
        Xmax = max(Xmax,x);
    }
    // median in O(n) in average via quickselect
    nth_element(Y.begin(),Y.begin()+N/2,Y.end());
    long long D = Xmax-Xmin;
    for (int i=0; i<N; ++i) D += abs(Y[i]-Y[N/2]);
    cout << D << endl;
    return 0;
}
