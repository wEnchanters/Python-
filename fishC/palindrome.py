def palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while right > left and not s[right].isalnum():
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


print(palindrome("aaab 12321 aa "))