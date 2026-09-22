from collections import Counter
class Solution:
    """
    The tasks that appear most often are the hardest to schedule.
    (n+1) * (max_freq -1)  + num_max
    max_freq - 1
    Each block has a length of n + 1 
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task.
        frequencies = Counter(tasks)

        # Find the highest frequency among all task types.
        max_freq = max(frequencies.values())

        #count how many types have the max freq
        num_max = list(frequencies.values()).count(max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + num_max
        )


