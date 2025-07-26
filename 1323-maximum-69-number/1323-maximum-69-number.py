class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        digit_num = len(digits)
        i = 0
        while (i<digit_num):
            if digits[i] == '6':
                digits[i] = '9'
                break
            i += 1
        return int(''.join(digits))