class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = [] 

        n = len(s)

        def dfs(start):
            if len(path) == 4:
                if start == n:
                    result.append(".".join(path))
        
            remaining_digits = n - start
            remaining_segments = 4 - len(path)

            if remaining_digits < remaining_segments:
                return 
            if remaining_digits > remaining_segments * 3:
                return
            
            for length in range(1, 4):
                    end = start + length

                    if end > n:
                        break
                    if length > 1 and s[start] == "0":
                        break
                    segment = s[start:end]

                    if int(segment) > 255:
                        break
                    path.append(segment)

                    dfs(end)

                    path.pop()
        dfs(0)
        return result



                
                
