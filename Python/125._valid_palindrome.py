def isPalindrome(s: str) -> bool:
    s = "".join([char for char in s if char.isalnum()]).lower()
    print(s)
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "0P"
print(isPalindrome(s))
