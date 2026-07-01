from Cell import Cell
from pygame import Surface

import random

class Grid():
    
    def __init__(self, height, width, birthCondition = [3,3], deathCondition = [1,4]):
        self.height = height
        self.width = width
        self.cells = [[Cell(state = bool(random.getrandbits(1)), birthCondition= birthCondition, deathCondition = deathCondition) for _ in range(0,width)] for _ in range(0,height)]
        for n, row in enumerate(self.cells):
            for m, cell in enumerate(row):
                cell.set_neighbours(self.get_cell_neighbours([n,m]))
        
                
    def in_grid(self,position):
        return (False if position[0] < 0 or position[0] >= self.height or position[1]<0 or position[1]>= self.width else True)
        
    def get_cell(self, position):
        return self.cells[position[0]][position[1]] if self.in_grid(position) else None
    
    def get_all_cells(self):
        cells = []
        for row in self.cells:
            for cell in row:
                cells.append(cell)
        return cells
        
    def set_cell_state(self, position, state):
        cell = self.get_cell(position)
        cell.set_state(state)
        
    def get_cell_neighbours(self, position):
        cell = self.get_cell(position)
        neighbourPositions = [
            [position[0]-1,position[1]-1],
            [position[0],position[1]-1],
            [position[0]+1,position[1]-1],
            [position[0]-1,position[1]],
            [position[0]+1,position[1]],
            [position[0]-1,position[1]+1],
            [position[0],position[1]+1],
            [position[0]+1,position[1]+1]]
        return [self.get_cell(pos) for pos in neighbourPositions if self.get_cell(pos)]
    
    def step(self):
        cells = self.get_all_cells()
        for cell in cells: cell.set_state(cell.get_new_state())
        for cell in cells: cell.update_new_state()
    
    def draw(self, screen_size):
        grid_surf = Surface((screen_size[0],screen_size[1]))
        grid_surf.fill("blue")
        cell_width = screen_size[0]//self.width
        cell_height = screen_size[1]//self.height
        
        for n, row in enumerate(self.cells):
            for m, cell in enumerate(row):
                    cell_left = m*cell_width
                    cell_top = n*cell_height
                    grid_surf.blit(cell.draw([cell_width,cell_height]), (cell_left, cell_top))
        
        return grid_surf
        
    def __str__(self):
        #return str([[str(cell) for cell in row] for row in self.cells])
        out =""
        for row in self.cells:
            out = out + str([str(cell) for cell in row]) + "\n"
        return out