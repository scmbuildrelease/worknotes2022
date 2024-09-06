


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_store = {}
        total = 0 
        count = 0 
        sum_store[0] = 1
        for num in nums:
            total += num
            if total - k in sum_store:
                count += sum_store[total-k]
            if total in sum_store:
                sum_store[total] += 1
            else:
                sum_store[total] = 1 
        return count
