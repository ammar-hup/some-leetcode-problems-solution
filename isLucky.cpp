bool solution(int n) {
    vector<int>v;
    while (n != 0) {
        v.push_back(n%10);
        n /= 10;
    }
    int count1 = 0, count2 = 0;
    for(int i = 0; i < v.size()/2; i++){
        count1 += v[i];
    }
    for(int i = v.size()-1; i > v.size()/2 - 1; i--){
        count2 += v[i];
    }
    return count1 == count2;
}
