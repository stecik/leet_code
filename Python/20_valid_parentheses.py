from queue import LifoQueue


def isValid(s: str) -> bool:
    stack = LifoQueue()
    map = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char not in map.keys():
            stack.put(char)
        else:
            if stack.empty() or stack.get() != map[char]:
                return False
    return stack.empty()
