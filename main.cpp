#include<bits/stdc++.h>
using namespace std;
int n,m;
vector<int>a,b;
void input(vector<int>&v,int size){
    for(int i=0;i<=size;i++){
        int temp;
        cin>>temp;
        v.push_back(temp);
    }
}
int main()
{
    cin>>n;
    input(a,n);
    cin>>m;
    input(b,m);
    vector<int>c;
    cout<<"Cal";
    int k=n+m;
    for(int i=0;i<=k;i++){
       for(int j=i;j>=0;j--){
         if(i-j<=m && j<=n){
            c[i]+=a[j]*b[i-j];
         }
       }
    }
    for(int i=0;i<=k;i++){
      cout<<c[i]<<" ";
    }
    return 0;
}
