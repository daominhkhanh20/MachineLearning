#include<bits/stdc++.h>
using namespace std;

struct bigNum{
   char sign;
   string number;
};

bigNum mul(bigNum a,bigNum b){
   int n=a.number.size();
   int m=b.number.size();
   int l=n+m;
   string temp;
   temp.resize(l);
   bigNum c;
   for(int i=0;i<n;i++){
      
      for(int j=0;j<m;j++){

      }
   }
   return c;
}
bigNum input(){
   bigNum c;
   string temp;
   cin>>temp;
   c.sign=temp[0];
   c.number=temp.substr(1,temp.size()-1);
   return c;
}
int main()
{
    bigNum a=input();
    bigNum b=input();
    cout<<a.sign<<" "<<a.number;
    bigNum c=mul(a,b);
    return 0;
}
