class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = ""
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()  

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(substring * num)

        return "".join(stack)