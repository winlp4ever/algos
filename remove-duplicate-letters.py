import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s

        # keep track of occurances of each character in the original string
        counter = collections.Counter(s)

        # keep track of which characters have already been used
        used = set()

        stack = []

        # iterate through the input string
        for ch in s:
            counter[ch] -= 1
            # skip current character
            # 1) if it is already in use
            if ch in used:
                continue

            # pop off characters from stack if they are larger than the current character
            # and there are other appearances of them later in the string
            while stack and stack[-1] > ch and counter[stack[-1]]:
                used.remove(stack.pop())

            # add this character onto the stack
            stack.append(ch)
            # mark this character as used
            used.add(ch)

        return ''.join(stack)