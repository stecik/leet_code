def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True
    if len(s) > len(t):
        return False
    i = 0
    for char in t:
        if s[i] == char:
            i += 1
        if i >= len(s):
            return True
    if i == len(s):
        return True
    return False


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))

s = ""
t = "ahbgdc"
print(isSubsequence(s, t))

s = "b"
t = "abc"
print(isSubsequence(s, t))
