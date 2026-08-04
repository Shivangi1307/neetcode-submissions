from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = defaultdict(list)
        emailToName = {}

        for account in accounts:
            name = account[0]
            firstemail = account[1]

            for email in account[1:]:

                emailToName[email] = name

                graph[firstemail].append(email)
                graph[email].append(firstemail)        

        visited = set()
        ans = []

        def dfs(email,emails):

            emails.append(email)
            visited.add(email)

            for neighbour in graph[email]:

                if neighbour not in visited:
                    dfs(neighbour,emails)

        for email in emailToName:
            if email not in visited:
                
                emails = []
                dfs(email,emails)
                ans.append([emailToName[email]] + emails)


        return ans
