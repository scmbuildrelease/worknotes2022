# 528. Random Pick with Weight

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.presum=[]
        presum=0
        self.sum=0
        for i in w:
            presum+=i
            self.presum.append(presum)
        self.sum=presum

    def pickIndex(self):
        """
        :rtype: int
        """
        target=random.random() * self.sum
        lo , hi= 0, len(self.presum)-1
        while lo<hi:
            mid=lo +(hi-lo)//2
            if self.presum[mid] < target:
                lo=mid +1
            else:
                hi=mid
        return lo
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


####
import random

class Solution:

    def __init__(self, w):
        self.prefix_sum = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix_sum.append(curr_sum)
        self.total_sum = curr_sum

    def pickIndex(self):
        # Generate a random number between 1 and total_sum (inclusive)
        target = random.randint(1, self.total_sum)
        
        # Linear search to find the corresponding index
        for i, prefix in enumerate(self.prefix_sum):
            if target <= prefix:
                return i
