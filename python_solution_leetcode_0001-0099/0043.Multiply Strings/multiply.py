class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
            
        res = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Calculate the product and add to the current position
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Join result, stripping the leading zero if it exists
        ans = "".join(map(str, res))
        return ans.lstrip("0")