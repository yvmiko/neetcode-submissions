class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:



        groups = {}

        for word in strs:
            counts = [0] * 26

            for character in word:
                index = ord(character) - ord("a")
                counts[index] += 1

            key = tuple(counts)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        result = []

        # for key in groups:
        #     result.append(groups[key])

        # return result
        return list(groups.values())
