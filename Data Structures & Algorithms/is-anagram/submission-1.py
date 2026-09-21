class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counts = {}

        for character in s:
            counts[character] = counts.get(character, 0) + 1

        for character in t:
            if character in counts:
                counts[character] -= 1
            else:
                return False

        for character in counts:
            if counts[character] != 0:
                return False

        return True


        