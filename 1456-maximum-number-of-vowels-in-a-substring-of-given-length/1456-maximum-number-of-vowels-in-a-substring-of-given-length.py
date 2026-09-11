class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowels = current_vowels
        
        # Early exit optimization
        if max_vowels == k:
            return k
        
        # Slide the window across the rest of the string
        for i in range(k, len(s)):
            # Add new character on the right
            if s[i] in vowels:
                current_vowels += 1
            # Remove old character on the left
            if s[i - k] in vowels:
                current_vowels -= 1
                
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                
            # If we hit the maximum possible vowels, we can stop early
            if max_vowels == k:
                return k
                
        return max_vowels
