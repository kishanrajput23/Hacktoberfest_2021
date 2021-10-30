#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin>> n;
    vector<int>v(n);
    for(int i = 0; i < n; i++)
    {
        cin>>v[i];
    }

    int search;
    cin>>search;
    int lo = 0, hi = n-1;
    int mid;

    while(hi-lo > 1){
        int mid = (hi+lo)/2;
        if(v[mid] < search){
            lo = mid + 1;
    } else {
        hi = mid;
    }
}
    if(v[lo] == search){
        cout<<lo<<endl;
    }
    else if(v[hi] == search){
        cout<<hi<<endl;
    }
    else{
        cout<<"Not Found";
    }
}
//Time Complexity
 // *log2(N)
