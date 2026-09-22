from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())

        #find num of task types share the max_freq
        num_max = list(freq.values()).count(max_freq)
#task schedule length 
        return max(len(tasks), (max_freq-1)*(n+1) + num_max)

        