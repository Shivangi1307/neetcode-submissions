class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length() - 1
        
        left, right = 0, n

        while left <= right:

            med = left + (right - left) //2

            if mountainArr.get(med) < mountainArr.get(med + 1):
                left = med + 1

            else:
                right = med - 1

        peak = left

        left = 0
        right = peak

        while left <= right:

            med = left + (right - left) //2
            val = mountainArr.get(med)

            if val == target:
                return med

            elif val < target:
                left = med + 1
            
            else:
                right = med - 1


        left = peak + 1
        right = n

        while left <= right:

            med = left + (right - left) //2
            val = mountainArr.get(med)

            if val == target:
                return med

            elif val < target:
                right = med - 1
            
            else:
                left = left + 1


        return -1