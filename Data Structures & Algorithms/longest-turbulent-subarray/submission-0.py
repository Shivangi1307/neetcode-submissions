class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        current = 1
        answer = 1

        for i in range(1,len(arr)):

            if arr[i] == arr[i-1]:
                current = 1

            elif i == 1 or arr[i-2] < arr[i-1] and arr[i-1] > arr[i] or arr[i-2] > arr[i-1] and arr[i-1] < arr[i]:
                current += 1

            else:
                current = 2

            answer = max(answer,current)


        return answer
