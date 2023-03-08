vector<int> solution(vector<int> a) {
    vector<int> sorted;
    for(auto o : a){
        if(o != -1)
            sorted.push_back(o);
    }
    sort(sorted.begin(),sorted.end());
    vector<int> ans;
    for (int i  = 0 , j = 0; i < a.size(); i++) {
        if(a[i] == -1)
            ans.push_back(-1);
        else {
            ans.push_back(sorted[j]);
            j++;
        }
    }
    return ans;
}
