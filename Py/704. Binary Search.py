class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(arr,l,r,target):
            if r >= l:
                mid = (r + l) // 2 
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return bs(arr,l,mid-1,target)
                else :
                    return bs(arr,mid+1,r,target)
            else :
                return -1
        return bs(nums, 0, len(nums)-1, target)
        
