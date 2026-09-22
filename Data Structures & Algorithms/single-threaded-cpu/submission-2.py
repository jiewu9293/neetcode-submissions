import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(enqueue_time, processing_time,index) for index,[enqueue_time,processing_time] in enumerate(tasks)]

        indexed_tasks.sort()
        n = len(tasks)
        #point to next unprocessed task
        task_index = 0
        current_time = 0
        min_heap = []
        result = []
        #if cpu have unprocessed tasks 
        while task_index < n or min_heap:
            #if cpu is idle jump to next task's time
            if not min_heap:
                current_time = max(
                    current_time,
                    indexed_tasks[task_index][0]
                )
            #while task is available to process
            while (task_index < n and indexed_tasks[task_index][0] <= current_time):
                #add tasks to heap
                enqueue_time, processing_time, original_index = indexed_tasks[task_index]

                heapq.heappush(min_heap,(processing_time,original_index))

                task_index +=  1
            processing_time, original_index = heapq.heappop(min_heap)

            current_time += processing_time
            result.append(original_index)
        return result




        
