class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both arrays so that we can match positions
        # from left to right without creating crossing assignments.
        seats.sort()
        students.sort()

        total_moves = 0

        # Match the i-th student with the i-th seat.
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        return total_moves