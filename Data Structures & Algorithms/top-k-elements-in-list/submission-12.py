from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        sorted_numbers = sorted(frequency,key=lambda                                 number:frequency[number],
        reverse=True) 

        return sorted_numbers[:k]


        