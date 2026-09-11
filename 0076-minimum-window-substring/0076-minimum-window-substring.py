class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = [0] * 128
        window_counts = [0] * 128

        required_unique = 0
        for i in range(len(t)):
            char_code = ord(t[i])
            if target_counts[char_code] == 0:
                required_unique += 1
            target_counts[char_code] += 1

        formed_unique = 0
        min_len = float("inf")
        start_idx = 0
        left = 0

        for right in range(len(s)):
            right_code = ord(s[right])
            window_counts[right_code] += 1

            if target_counts[right_code] > 0 and window_counts[right_code] == target_counts[right_code]:
                formed_unique += 1

            while formed_unique == required_unique:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    start_idx = left

                left_code = ord(s[left])
                window_counts[left_code] -= 1
                
                if target_counts[left_code] > 0 and window_counts[left_code] < target_counts[left_code]:
                    formed_unique -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start_idx : start_idx + min_len]