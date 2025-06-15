class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            def bs(nums,target,isLeft):
                left , right = 0 , len(nums)-1
                idx = -1
                while left<=right:
                    mid = (left+right)//2
                    if nums[mid]>target:
                        right = mid-1
                    elif nums[mid]<target:
                        left = mid+1
                    else:
                        idx = mid
                        if isLeft:
                            right=mid-1
                        else:
                            left=mid+1
                return idx
            left = bs(nums,target,True)
            right = bs(nums,target,False)
            return [left,right]

                