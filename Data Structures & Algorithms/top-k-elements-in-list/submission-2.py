class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Which K values show up the most in an array"""

        # create a hash map to check for num frequencies
        count: dict[int, int] = {}

        for num in nums:
            # if num in count:
            #     count[num] += 1
            # else:
            #     count[num] = 1
            count[num] = 1 + count.get(num, 0)

        # the bucket groups the nums
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        # distribute the nums into the buckets
        for num in count:
            freq = count[num]
            bucket[freq].append(num)

        
        
        result = []
        for freq in range(len(bucket) -1, 0, -1):
            for num  in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
