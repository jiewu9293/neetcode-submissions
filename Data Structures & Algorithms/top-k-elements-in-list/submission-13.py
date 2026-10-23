class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        sorted_number = sorted(frequency,key= lambda num:frequency[num],reverse=True)
        return sorted_number[:k]