class Solution(object):
    def sortArray(self, nums):
        def heapify(arr,n,i):
            largest = i
            left = i*2+1
            right = i*2+2

            if left<n and arr[i]<arr[left]:
                largest = left
            if right<n and arr[largest]<arr[right]:
                largest = right
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(arr,n,largest)
        n=len(nums)
        for i in range(n//2,-1,-1):
            heapify(nums,n,i)

        for i in range(n-1,0,-1):
            nums[i],nums[0] = nums[0],nums[i]
            heapify(nums,i,0)
        return nums
        