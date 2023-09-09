class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lis = sorted(nums)
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
        if bs(lis, 0, len(lis)-1, target) :
            for i in range(len(nums)):
                if nums[i] == target :
                    return i
        else :
            return -1
