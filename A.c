#define _local_debug_

#include <stdio.h>
#include <time.h>

void solve(){
    printf("Yes");
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        #ifdef _local_debug_
            clock_t start = clock();
        #endif
        solve();
        #ifdef _local_debug_
            clock_t end = clock();
            printf("Case #%d: %lf ms\n", i, (double)(end - start) / CLOCKS_PER_SEC * 1000);
        #endif
    }
    return 0;
}