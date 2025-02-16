from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix_len = 0
    prefix = ""
    if not any(strs):
        return prefix
    min_len_word = min(strs)
    max_len = len(min_len_word)
    while prefix_len < max_len:
        prefix_len += 1
        prefix = min_len_word[:prefix_len]
        for s in strs:
            if not s.startswith(prefix):
                return prefix[: prefix_len - 1]
    return prefix[:prefix_len]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))

strs = ["dog", "dog", "dog"]
print(longestCommonPrefix(strs))

strs = []
print(longestCommonPrefix(strs))

strs = [""]
print(longestCommonPrefix(strs))

strs = ["", "b"]
print(longestCommonPrefix(strs))

strs = ["cir", "car"]
print(longestCommonPrefix(strs))

strs = ["a"]
print(longestCommonPrefix(strs))
