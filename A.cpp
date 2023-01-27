#define _local_debug_

#include <bits/stdc++.h>
using namespace std;

void solve(){
    cout << "Yes" << endl;
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        #ifdef _local_debug_
            clock_t start = clock();
        #endif
        solve();
        #ifdef _local_debug_
            clock_t end = clock();
            cout << "Case #" << i << ": " << (double)(end - start) / CLOCKS_PER_SEC * 1000 << " ms" << endl;
        #endif
    }
    return 0;
}