class Solution:
    count = 0
    def cal(self, N, pos, visited):
        if pos > N:
            self.count += 1
        for i in range(1, N+1):
            if (not visited[i]) and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.cal(N, pos+1, visited)
                visited[i] = False
    def countArrangement(self, N: int) -> int:
        visited = [False for _ in range(N+1)]
        self.cal(N, 1, visited)
        return self.count