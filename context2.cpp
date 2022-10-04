
#include <bits/stdc++.h>

using namespace std;

// Using long long instead of int to avoid overflow
// defines to reduce typing
#define ll long long
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()

// typedefs to reduce typing
typedef vector<int> vi;
typedef pair<int, int> pi;

//硬币找零问题(负数)
//有N枚硬币，每枚硬币有一个面值a[i](-1e5<=a[i]<=1e5)，问最少需要多少个硬币，才能组合出目标面值amount(-1e5<=a[i]<=1e5)
//注意每个硬币只能使用一次。
//coins:硬币面额列表
//amount:目标金额
//返回最少需要多少个硬币
//如果不能组合成amount,返回-1
//coins中可以有负数面额
//coins中可以有重复的面额
//amount可以为负数
int coin_exchange_nagative(vector<int> coins,int amount){
    //dp[i]表示组合出金额i所需要的最少硬币数
    //dp[i]=min(dp[i],dp[i-coins[j]]+1)
    //dp[0]=0
    //dp[i]=1e9+7
    //dp[amount]即为答案
    //dp定义为哈希表
    unordered_map<int,int> dp;
    int n=coins.size();
    int max_amount=1e5;
    int min_amount=-1e5;
    int inf=1e9+7;
    for(int i=min_amount;i<=max_amount;i++){
        dp[i]=inf;
    }
    dp[0]=0;
    for(int i=min_amount;i<=max_amount;i++){
        for(int j=0;j<n;j++){
            if(i-coins[j]>=min_amount){
                dp[i]=min(dp[i],dp[i-coins[j]]+1);
            }
        }
    }
    if(dp[amount]==inf){
        return -1;
    }
    return dp[amount];
}

//测试
int main(){
    vector<int> coins={1,2,5};
    int amount=11;
    cout<<coin_exchange_nagative(coins,amount)<<endl;
    return 0;
}