class Solution:
    def romanToInt(self, s: str) -> int:

        counter = 0
        number = 0
        while counter < len(s):
            if s[counter] == "I":
                if counter + 1 == len(s):
                    number += 1
                elif s[counter + 1] == "I":
                    number += 1
                elif s[counter + 1] == "V":
                    number += 4
                    counter += 1
                elif s[counter + 1] == "X":
                    number += 9
                    counter += 1
            elif s[counter] == "V":
                number += 5
            elif s[counter] == "X":
                if counter + 1 == len(s):
                    number += 10
                elif s[counter + 1] == "L":
                    number += 40
                    counter += 1
                elif s[counter + 1] == "C":
                    number += 90
                    counter += 1
                else:
                    number += 10
            elif s[counter] == "L":
                number += 50
            elif s[counter] == "C":
                if counter + 1 == len(s):
                    number += 100
                elif s[counter + 1] == "D":
                    number += 400
                    counter += 1
                elif s[counter + 1] == "M":
                    number += 900
                    counter += 1
                else:
                    number += 100

            elif s[counter] == "D":
                number += 500
            elif s[counter] == "M":
                number += 1000
            counter += 1

        return number
