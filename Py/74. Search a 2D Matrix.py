class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(arr,l,r,target):
            if r >= l:
                mid = (r + l) // 2 
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    return bs(arr,l,mid-1,target)
                else :
                    return bs(arr,mid+1,r,target)
            else :
                return False
        lis = []
        for i in range (len(matrix)):
            for j in range(len(matrix[i])):
                lis.append(matrix[i][j])
        return bs(lis, 0, len(lis)-1, target)
        
