class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        continent = set()
        for i in range(m):
            for j in range(n):
                continent.add((i,j))
        
        def okryj(x):
            a = []
            i = x[0]
            j = x[1]
            if i != 0:
                if grid[i-1][j] == "1":
                    a.append((i-1,j))
            if j != (n-1):
                if grid[i][j+1] == "1":
                    a.append((i,j+1))
            if i != (m-1):
                if grid[i+1][j] == "1":
                    a.append((i+1,j))
            if j != 0:
                if grid[i][j-1] == "1":
                    a.append((i,j-1))
            return a 
        
        ostrova = []
        
        def creator(x):  #создаёт остров по 1 его точке x = (i, j). И добавляет его в ostrova
            ostrov = {x}
            bil = []
            def poisk(x):
                if x in bil:
                    return 0
                bil.append(x)
                sosedi = okryj(x)
                for sosed in sosedi:
                    ostrov.add(sosed)
                for sosed in sosedi:
                    poisk(sosed)
            poisk(x)
            ostrova.append(ostrov)
            return ostrov
        

        def f(continent):
            if len(continent) == 0:
                return 0
            bil = set()
            for x in continent:
                bil.add(x)
                if grid[x[0]][x[1]] == "0":
                    continue
                ostrov = creator(x)
                continent -= ostrov
                continent -= bil
                bil.clear()
                break
            if len(bil) > 0: # значит мы вышли из цикла не найдя суши
                return 0
            f(continent)
            
        f(continent)
        self.ostrova = ostrova 
        return len(ostrova)

    
def main():
    import random
    import sys
    sys.setrecursionlimit(10000)
    m = 100
    n = 200
    grid = []
    for i in range(m):
        strok = []
        for j in range(n):
            strok.append(str(random.randint(0,1)))
        grid.append(strok)
    sol = Solution()
    print("число островов = ", sol.numIslands(grid))
    sol.ostrova.sort(key = lambda x: len(x))

    for i in sol.ostrova:
        print(i)

    print("Максимальная площадь острова ", len(sol.ostrova[-1]))
        

if __name__ == "__main__":
    main()









    
                
