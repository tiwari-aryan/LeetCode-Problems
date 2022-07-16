class Solution:
    def intToRoman(self, num: int) -> str:

        numeral = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        counter = 0
        numeral_string = ""
        while num != 0:
            if num < numbers[counter]:
                counter += 1
            else:
                num -= numbers[counter]
                numeral_string += numeral[counter]
        return numeral_string
