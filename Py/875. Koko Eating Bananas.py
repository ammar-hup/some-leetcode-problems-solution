class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r =  max(piles)
        while l<r:
            mid=(l+r)//2
            curr_speed = 0
            for p in piles:
                curr_speed += math.ceil(p / mid)
            if curr_speed > h:
                l = mid+1
            else:
                r = mid
        return l
