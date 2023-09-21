class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, idx, path, ans):
            ans.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1] :
                    continue 
                dfs(nums, i+1, path+[nums[i]], ans)
            
        ans = []
        dfs(sorted(nums),0,[],ans)
        return ans
