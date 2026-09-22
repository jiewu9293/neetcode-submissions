class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add the original index to every task.
        indexed_tasks = [
            (enqueue_time, processing_time, index)
            for index, (enqueue_time, processing_time) in enumerate(tasks)
        ]

        # Sort tasks by enqueue time.
        indexed_tasks.sort()
        min_heap = []
        n = len(indexed_tasks)
        answer = []
        current_time = 0
        task_index = 0
        # The heap stores:
        # (processing_time, original_index)
        #while we have unprocessed tasks or tasks in heap
        while task_index < n or min_heap:
            #if cpu idle
            #update current time if the next task in future
            #unchanges if the next task is arrived
            if not min_heap:
                current_time = max(
                    current_time,
                    indexed_tasks[task_index][0]
                )
            # while task is unprocesssed and ready to process add the tasks to heap
            while (task_index < n and indexed_tasks[task_index][0] <= current_time):
                enqueue_time, processing_time, original_index = (
                    indexed_tasks[task_index]
                )
                heapq.heappush(
                    min_heap,
                    (processing_time, original_index)
                )
                #move pointer to next task to process
                task_index += 1
                # Choose the task with the shortest processing time.
                # If there is a tie, choose the one with the smallest index.
            processing_time, original_index = heapq.heappop(min_heap)

            # Run the selected task until it is completed.
            current_time += processing_time
            answer.append(original_index)
        return answer




                

