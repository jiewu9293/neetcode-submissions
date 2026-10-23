class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value is ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)

                if(value in rows[row] or value in columns[col]or value in boxes[box_index]):
                    return False

                rows[row].add(value)
                columns[col].add(value)
                boxes[box_index].add(value)
        return True      

                