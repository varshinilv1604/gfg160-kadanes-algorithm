class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        n=len(arr)
        if n==0:
            return 0
        current=arr[0]
        best=arr[0]
        for i in range(1,n):
            current=max(arr[i],arr[i]+current)
            if(current>best):
                best=current
        return best