class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=lambda x: x[1])  # Classificar os trabalhos pelo tempo de término.

        dp = [0] * len(jobs)  # Inicializar uma lista de tamanho igual ao número de trabalhos.

        def binary_search(end_time):
            left, right = 0, len(jobs) - 1
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][1] <= end_time:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        dp[0] = jobs[0][2]  # Lucro do primeiro trabalho.

        for i in range(1, len(jobs)):
            current_profit = jobs[i][2]
            last_compatible_job = binary_search(jobs[i][0])

            if last_compatible_job != -1:
                current_profit += dp[last_compatible_job]

            dp[i] = max(current_profit, dp[i - 1])

        return dp[-1]  # O último elemento contém o lucro máximo.
