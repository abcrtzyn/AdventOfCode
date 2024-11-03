import numpy as np

rolls = [(-1,-1),(-1, 0),(-1, 1),
         ( 0,-1),        ( 0, 1),
         ( 1,-1),( 1, 0),( 1, 1)]

totalCount = 0

with open("input.txt",'r') as f:
    grid = np.array([[int(i) for i in list(s.strip())] for s in f.readlines()],np.uint8)
    grid = np.pad(grid, 1, 'constant', constant_values=0)
    # one time step
    i = 0
    while True:

        grid = grid + np.ones(grid.shape, np.uint8)
        
        over9 = np.pad(grid[1:-1,1:-1] > 9, 1, 'constant', constant_values=False)
        previousCount = 0
        count = over9.sum()
        previousOver9 = np.zeros(grid.shape,dtype=np.bool8)
        
        while count != previousCount:
            increment = over9 ^ previousOver9
            for roll in rolls:
                grid = grid + np.roll(increment, roll, (0,1))
                
            previousOver9 = over9
            previousCount = count
            over9 = np.pad(grid[1:-1,1:-1] > 9, 1, 'constant', constant_values=False)
            count = over9.sum()
        grid = grid * ~over9 #reset all flashed to 0
        i += 1
        if count == 100:
            print(i)
            break
        totalCount += count
    print(totalCount)


    
    