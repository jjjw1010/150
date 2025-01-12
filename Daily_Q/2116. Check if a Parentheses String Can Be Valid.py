class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        str_len = len
        # if s is odd length, invalid -> False
        if len(s)%2 != 0: return False

        # s has to be even in length 
        open_ind = []
        unlocked_ind = []

        for i in range(str_len):
            if locked[i] == '0':
                unlocked_ind.append(i)
            # for locked[i] == 1,
            elif s[i] == "(" :
                open_ind.append(i)
            elif s[i] == ")" :
                # Pop the closest previous available open ind
                if open_ind :
                    open_ind.pop()
                # Pop the closest previous available wildcard
                elif unlocked_ind:
                    unlocked_ind.pop()
                else:
                # No matching pair found
                    return False
        
        while open_ind and unlocked_ind and open_ind [-1] < unlocked_ind [-1]:
            open_ind.pop()
            unlocked_ind.pop()

        if not open_ind and unlocked_ind:
            return len(unlocked_ind) % 2 == 0
        
        return not open_ind
