from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            source, dest = ticket
            graph[source].append(dest)

        for source in graph:
            graph[source].sort(reverse=True)

        def dfs(node):
            while graph[node]:
                next_dest = graph[node].pop()
                dfs(next_dest)
            result.append(node)

        result = []
        dfs("JFK")

        return result[::-1]
