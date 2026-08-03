from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        graph = defaultdict(list)

        for prereq,course in prerequisites:
            graph[course].append(prereq)

        prereqMap = {}
        
        def dfs(course):

            if course in prereqMap:
                return prereqMap[course]


            prereqs = set()

            for prereq in graph[course]:

                prereqs.add(prereq)
                prereqs |= dfs(prereq)

            prereqMap[course] = prereqs  

            return prereqs


        for course in range(numCourses):
            dfs(course)

        ans = []

        for prereq,course in queries:
            ans.append(prereq in prereqMap[course])


        return ans