class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            next_result = []
            index = 0

            while index < len(result):
                count = 1
                while index + count < len(result) and result[index] == result[index + count]:
                    count += 1

                next_result.append(str(count))
                next_result.append(result[index])
                index += count

            result = "".join(next_result)

        return result