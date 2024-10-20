from collections import defaultdict
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj_list = defaultdict(list)

        for prereq in prerequisites:
            indegrees[prereq[0]] += 1
            adj_list[prereq[1]].append(prereq[0])
        q = deque([])
        count = 0

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        while q:
            curr = q.popleft()

            for neigh in adj_list[curr]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    q.append(neigh)
                    count += 1
                    if count == numCourses:
                        return True
        return count == numCourses


# time complexity is O(V+E) where V(vertices) is number of courses and E(edges)is the number of prerequisites
# space complexity is O(V+E) where V(vertices) is number of courses and E(edges)is the number of prerequisites
