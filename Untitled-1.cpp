#include<bits/stdc++.h>

using namespace std;

//for storing the count of each character in both substrings
int dp1[27],dp2[27];

int main() {

//taking string as input
string s;
cin>>s;
//storing the length of given string
int n=s.length();

int i,j,k,l;

//keeping the count of each character of second substring
for(i=0;i<n;i++){
dp2[s[i]-'a']++;
}

//for storing the answer
int ans=0;
//moving each character from second substring to the first substring
//and calculating the number of common characters
for(i=0;i<n;i++){
char c=s[i];
dp1[c-'a']++;
dp2[c-'a']--;
int tmp=0;
for(j=0;j<26;j++){
tmp+=min(dp1[j],dp2[j]);
}
//updating the answer
ans=max(ans,tmp);
}

//displaying the answer
cout<<ans;

return 0;
}​