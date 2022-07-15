class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        negative = 1
        number = False
        num = ""
        s = s.strip()
        for i in s:
            if i not in numbers:
                if i != "+" and i != "-" or number == True:
                    break
                else:
                    if i == "-":
                        negative = -1
                    number = True
            else:
                number = True
                num += i
        power = len(num) - 1
        int_num = 0
        for i in num:
            int_num += int(i) * 10**power
            power -= 1
        if int_num * negative < -(2**31):
            return -(2**31)
        elif int_num * negative > 2**31 - 1:
            return 2**31 - 1
        else:
            return int_num * negative
