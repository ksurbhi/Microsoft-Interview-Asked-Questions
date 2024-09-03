from queue import Queue
class Solution:
    """
    Using BFS
    Time: O(M*N)
    Space: (M*N)
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) ==0:
            return 0
        q = Queue()
        dirs = [[-1,0],[1,0],[0,-1],[0,1]] #U, D, L,R
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count +=1
                    q.put([i,j])
                    grid[i][j] = '2'                    
                    while not  q.empty():
                        curr = q.get()
                        for Dir in dirs:
                            nr = curr[0]+Dir[0]
                            nc = curr[1]+Dir[1]
                            if 0<= nr <len(grid) and 0<= nc <len(grid[0]) and grid[nr][nc]=='1':
                                grid[nr][nc]='2'
                                q.put([nr,nc])
        return count


        
########## Using DFS ##########
class Solution:
    """
    Using DFS
    Time: O(M*N)
    Space: (M*N)
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        if grid == None or len(grid) ==0:
            return 0
        count = 0
        self.dirs = [[-1,0],[1,0],[0,-1],[0,1]] #U, D, L,R
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count +=1
                    self.dfs(grid,i,j)
        return count

    def dfs(self, grid: List[List[str]],row:int,col:int):
        # base case
        if row <0 or row >=len(grid) or col <0 or col >=len(grid[0]) or grid[row][col] != '1':
            return
        grid[row][col] = '2'
        for Dir in self.dirs:
            nr = row + Dir[0]
            nc = col + Dir[1]
            self.dfs(grid,nr,nc)

