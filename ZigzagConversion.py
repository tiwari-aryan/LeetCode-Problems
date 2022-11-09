class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(0, numRows)]
        counter = 0

        string = ""
        index = 1
        for i in s:
            rows[counter].append(i)
            counter += index
            if counter >= numRows:
                counter = numRows - 2
                index *= -1
            elif counter < 0:
                index *= -1
                counter = 1
        for i in rows:
            string += "".join(i)
        return string
