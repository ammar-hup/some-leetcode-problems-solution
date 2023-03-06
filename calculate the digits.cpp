vector<int> solution(vector<int> a) {
    vector<int> b;
    
    for(int i = 0; i < a.size(); i++){
        while(a[i] != 0){
            b.push_back(a[i] % 10);
            a[i] /= 10;
        }
    }
    
    int freq[1001] = {0};
    
    for(auto o : b) freq[o]++;
    
    int mx = *max_element(freq, freq + 1001);
    
    set<int> s;
    
    for(auto o : b) {
        if (freq[o] == mx){
            s.insert(o);
        }   
    }
    
    vector<int> ans;
    for(auto o : s) {
        ans.push_back(o);
    }
    
    return ans;
}
int main()
{
    vector<int> a{989};
    vector<int> x;
    x = solution(a);
    for (auto o : x) cout << o << " ";
    return 0;
}
