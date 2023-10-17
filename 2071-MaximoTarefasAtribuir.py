from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_assign_tasks(task_requirements, available_workers, remaining_pills, required_strength, num_tasks):
            task_idx = 0
            unassigned_tasks = []
            for worker_idx in range(num_tasks - 1, -1, -1):
                while task_idx < num_tasks and task_requirements[task_idx] <= available_workers[worker_idx] + required_strength:
                    unassigned_tasks.append(task_requirements[task_idx])
                    task_idx += 1

                if not unassigned_tasks:
                    return False

                if available_workers[worker_idx] >= unassigned_tasks[0]:
                    unassigned_tasks.pop(0)
                elif remaining_pills > 0:
                    unassigned_tasks.pop()
                    remaining_pills -= 1
                else:
                    return False

            return True

        tasks.sort()
        workers.sort(reverse=True)

        left = 0
        right = min(len(tasks), len(workers))
        max_assigned_tasks = -1

        while left <= right:
            mid = (left + right) // 2

            if can_assign_tasks(tasks, workers, pills, strength, mid):
                max_assigned_tasks = mid
                left = mid + 1
            else:
                right = mid - 1

        return max_assigned_tasks
