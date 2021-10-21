#include <iostream>
#include <cstdio>
#include<bits/stdc++.h>
#include <algorithm> 
#define ll long long int
using namespace std;
const int MOD = 1e9 + 7;
const int N = 1000000;
int cc_size = 0;

ll fast_pow(ll x , ll y)
{
    if(y == 0)
        return 1;
    ll z = fast_pow(x, y/2);
    z = (z*z)%MOD;
    
    if(y%2!=0)
        z = (z*x) % MOD;
        
    return z;
    
}
void dfs(int i , vector<bool>& vis , vector<int> g[])
{
    vis[i] = true;
    cc_size++;
    for(int x : g[i])
    {
        if(!vis[x])
        {
            dfs(x, vis, g);
        }
    }
}

int main() {
        
    int n , k;
    cin>>n>>k;
    
    vector<int> g[N];
    
    for(int i = 0;i<n-1;i++)
    {
        ll u,v,x;
        cin>>u>>v>>x;
        if(x == 0)
        {
            g[u].push_back(v);
            g[v].push_back(u);
        }
        
    }
    int ans = fmod(fast_pow(n , k) , MOD);
    
    vector<bool> vis(N,false);
    
    for(int i = 1;i<=n ;i++)
    {
        if(!vis[i])
        {
            cc_size = 0;
            dfs(i, vis, g);
            
            ans = ans - fast_pow(cc_size ,k) +  MOD;
            ans %= MOD; 
        }
    }
    cout<<ans<<endl;
    return 0;
}
