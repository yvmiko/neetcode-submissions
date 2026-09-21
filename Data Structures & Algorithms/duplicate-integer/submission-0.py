class Solution:
    def hasDuplicate(self, numbers: List[int]) -> bool:

        seen_numbers = set()

        for number in numbers:
            if number in seen_numbers:
                return True
            
            seen_numbers.add(number)
        
        return False
        