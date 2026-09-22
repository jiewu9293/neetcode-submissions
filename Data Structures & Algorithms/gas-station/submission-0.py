class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 
        total_tank = 0
        current_tank = 0
        for i in range(len(gas)):
            # Net amount of gas gained at station i
            gain = gas[i] - cost[i]

            # Track whether the total gas is enough for the whole circuit
            total_tank += gain

            # Track whether the current starting point can reach the next station
            current_tank += gain
            #we choose a new start positino
            if current_tank < 0:
                start = i + 1
                #reset current tank
                current_tank = 0
        return start if total_tank >= 0 else -1 
        