class Solution:
    def isValid(self, s: str) -> bool:

        # We will use a stack for this problem
        stack = []

        # and a hashmap to match the closing characters to their corresponding open characters
        close_to_open = {')' : '(', 
                         '}' : '{', 
                         ']' : '['}

        # For each character in our input string
        for c in s:
            # If it's a closing character
            if c in close_to_open:
                # and the stack ISNT empty, and if the top of the stack is the
                # matching open character
                if stack and stack[-1] == close_to_open[c]:
                    # we have a match and we can pop
                    stack.pop()
                # but if the stack is empty, or it's not a matching open character
                else:
                    # we can cut it here and return false
                    return False
            # Otherwise, if we have an opening character
            else:
                # We should add it to our stack
                stack.append(c)

        # We can only return true if the stack is empty, because that would indicate
        # we found a match for every character
        # This helps us with cases such as s = "(("
        return True if not stack else False