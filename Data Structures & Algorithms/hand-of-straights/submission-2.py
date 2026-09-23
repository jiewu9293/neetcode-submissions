from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
         # All groups must have exactly groupSize cards.
        if len(hand) % groupSize != 0:
            return False

         # Count the frequency of every card value.
        frequency = Counter(hand)

        # Process card values from smallest to largest
        for start in sorted(frequency):
            # All remaining copies of 'start' must begin new groups.
            groups_to_start = frequency[start]

            if groups_to_start == 0:
                continue
            
            for card in range(start, start + groupSize):
                if frequency[card] < groups_to_start:
                    return False

                frequency[card] -= groups_to_start
        return True