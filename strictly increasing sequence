bool solution(std::vector<int> sequence) {
    // 1 3 2 1 
    int i = INT_MIN, j = INT_MIN;
    int count = 0;
    for (auto n : sequence) {
        if (n <= i) {
            count++;
            if (n > j)
                i = n;
        } else {
            j = i;
            i = n;
        }
    }
    return count <= 1;
}
