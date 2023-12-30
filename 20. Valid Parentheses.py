class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initution: Use stack to add corresponding closing bracket when reading
        # opening bracket and when reading closing bracket to check if it is the right
        # one through poping stack
        # Keyword: order?
        stack = []
        paren_map = {"{":"}", "[":"]", "(":")"}
        paren_map_keys = paren_map.keys()
        for char in s:
            if char in paren_map_keys:
                stack.append(paren_map[char])
            else:
                if not stack: return False
                closing_paren = stack.pop()
                if closing_paren != char:
                    return False
        return len(stack) == 0