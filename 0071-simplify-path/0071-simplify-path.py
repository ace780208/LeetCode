class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_parts = path.split('/')
        for part in path_parts:
            if part in ['.', '']:
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return  '/'+'/'.join(stack)