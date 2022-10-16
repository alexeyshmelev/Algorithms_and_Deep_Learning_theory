class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            copy_x = x
            new_x = 0
            while x >= 1:
                last_d = x % 10
                x //= 10
                new_x = new_x * 10 + last_d
            if new_x == copy_x:
                return True
            else:
                return False