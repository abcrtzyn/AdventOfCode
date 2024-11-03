from typing import List


UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

TURN_RIGHT = {UP:RIGHT,RIGHT:DOWN,DOWN:LEFT,LEFT:UP}
TURN_LEFT  = {UP:LEFT,LEFT:DOWN,DOWN:RIGHT,RIGHT:UP}




class Virus:
    
    def __init__(self,grid:List[List[int]]):
        self.grid = grid
        self.position = (12,12)
        self.direction = UP

    def burst(self):
        mark = False

        if self.grid[self.position[0]][self.position[1]]:
            self.direction = TURN_RIGHT[self.direction]
            self.grid[self.position[0]][self.position[1]] = False
        else:
            self.direction = TURN_LEFT[self.direction]
            self.grid[self.position[0]][self.position[1]] = True
            mark = True
        # move forward
        self.

        return mark
        