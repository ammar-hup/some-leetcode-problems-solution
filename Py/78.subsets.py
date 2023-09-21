class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, idx, path, ans):
            ans.append(path)
            for i in range(idx, len(nums)):
                dfs(nums, i+1, path+[nums[i]], ans)
            
        ans = []
        dfs(sorted(nums),0,[],ans)
        return ans
