class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts: dict[int, int] = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # create bucket to store bucket lists
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        # distribute the numbers into the buckets
        for num in counts:
            freq = counts[num]
            buckets[freq].append(num)

        #
        result = []
        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                if len(result) < k:
                    result.append(num)

        return result
