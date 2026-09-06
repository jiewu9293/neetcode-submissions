class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time = (target - position) / speed
        #time taken for each car to location
        """
        [
        (pos,spd)
        ]
        stack store time taken for each car fleet to target
        time taken for car in front. 
        time taken for car behind 
        """
        cars = sorted(
        zip(position, speed),
        reverse=True,
    )
        stack = []
        for current_position, current_speed in cars:
            arrival_time = (
            target - current_position
        ) / current_speed
        #car behind can not catch up #form car fleet itself
            stack.append(arrival_time)
            if (
                len(stack) >= 2
                # compare time taken for car behind car in front
                and stack[-1] <= stack[-2]
            ):
                #able to from a car fleet 
                #car behind will catch up car in front
                stack.pop()
        return len(stack)
        


