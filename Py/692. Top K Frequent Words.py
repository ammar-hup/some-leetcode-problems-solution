class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(dict(sorted(Counter(words).items(), key = lambda x : (-x[1], x[0]))).keys())[:k]
