def isPalindrome(string):
    # Write your code here.

    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindrome(string):
    # Write your code here.
    if len(string) == 1 or string == "":
        return True
    if string[0] != string[len(string) - 1]:
        return False
    else:
        return isPalindrome(string[1 : len(string) - 1])
