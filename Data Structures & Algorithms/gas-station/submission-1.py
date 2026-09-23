class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        current_tank = 0
        total_tank = 0
        for i in range(len(gas)):
            gas_gained = gas[i] - cost[i]

            current_tank += gas_gained

            total_tank += gas_gained

            if current_tank < 0:
                start = i +1 
                current_tank = 0
        return start if total_tank >= 0 else -1 
            

