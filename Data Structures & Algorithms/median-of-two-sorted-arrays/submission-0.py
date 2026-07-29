class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        x = len(nums1)
        y = len(nums2)

        left = 0
        right = x

        while left <= right:

            partx = (left + right) // 2
            party = (x+y+1) // 2 - partx

            maxLeft_x = float('-inf') if partx == 0 else nums1[partx - 1]
            minRight_x = float('inf') if partx == x else nums1[partx]

            maxLeft_y = float('-inf') if party == 0 else nums2[party - 1]
            minRight_y = float('inf') if party == y else nums2[party]

            if maxLeft_x <= minRight_y and maxLeft_y <= minRight_x:

                if (x + y) % 2:
                    return max(maxLeft_x,maxLeft_y)

                return (
                    max(maxLeft_x,maxLeft_y) + 
                    min(minRight_x, minRight_y)  
                ) /2

            elif maxLeft_x > minRight_y:
                right = partx - 1
            else:
                left = partx + 1
