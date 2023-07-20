#include <bits/stdc++.h>

using namespace std;
long long solution(vector<int> a) {
    
    vector<string> b;
    
    for(int i = 0; i < a.size(); i++){
        string s = to_string(a[i]);
        b.push_back(s);
    }
    
    vector<string> vs;
    
    for(int i = 0; i < b.size(); i++){
        for(int j = 0; j < b.size(); j++){
            vs.push_back(b[i] + b[j]);
        }
    }
    vector<long long> v;
    
    for(int i = 0; i < vs.size(); i++){
        long long x = stol(vs[i]);
        v.push_back(x);
    }
    
    unsigned long long ans= 0;
    for(auto o : v) ans += o;
    
    return ans;
}

int main()
{
    vector<int> a{1000000, 1000000, 1000000, 1000000};
    cout << solution(a);
    return 0;
}
