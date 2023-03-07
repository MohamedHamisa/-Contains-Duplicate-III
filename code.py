class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}
        for i, num in enumerate(nums):
            v = num // (t + 1)
            for bucket in range(v - 1, v + 2):
                if bucket in buckets and abs(buckets[bucket] - num) <= t: return True
            buckets[v] = num
            if(len(buckets) > k): buckets.pop(next(iter(buckets))) 
        return False        

               



