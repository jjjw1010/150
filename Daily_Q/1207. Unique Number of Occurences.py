class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Initution: Use a hash_map to keep track of frequency
        freq_map = {}
        for num in arr:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        freq_freq_map = {}
        for _, value in freq_map.items():
            if value not in freq_freq_map:
                freq_freq_map[value] = 1
            else:
                return False
        return True