from pygame import Surface, Rect, draw, mouse

class Cell():
    state: bool = False
    neighbours: list = []
    newState: bool = False
    birthCondition:list = []
    deathCondition:list = []
    
    def __init__(self, x, y, w, h, life_colour, death_colour, state=False, neighbours:list = [], birthCondition = [3,4], deathCondition = [2,6]):

        #Location and Colour
        self.rect = Rect(x, y, w, h)
        third_width = w//3 if w>3 else 1
        third_height = h//3 if h>3 else 1
        self.next_indicator = Rect(x + third_width, y+third_height, third_width, third_height)
        self.life_colour = life_colour
        self.death_colour = death_colour

        #Set Initial Values
        self.state=state
        self.newState=state
        self.neighbours = neighbours
        
        #Calculate birth and Death conditions
        self.update_birth_conditions(birthCondition[0], birthCondition[1])
        self.update_death_conditions(deathCondition[0], deathCondition[1])
       
    
    def get_state(self):
        return self.state
    
    def set_state(self, state:bool):
        self.state = state
    
    def get_new_state(self):
        return self.newState
    
    def set_new_state(self, newState:bool):
        self.newState = newState
    
    def update_new_state(self):
        livingNeighbours = [neighbour.get_state() for neighbour in self.neighbours].count(True)
        if livingNeighbours in self.birthCondition: self.newState = True
        elif livingNeighbours in self.deathCondition: self.newState = False
    
    def get_neighbours(self):
        return self.neighbours
        
    def set_neighbours(self, neighbours):
        self.neighbours=neighbours
    def get_birth_conditions(self):
        return self.birthCondition
    
    def set_birth_conditions(self, conditions:list):
        self.birthCondition = conditions
    
    def update_birth_conditions(self, lowerLimit, higherLimit):
        self.birthCondition = [n for n in range(lowerLimit, higherLimit+1)]
    
    def get_death_conditions(self):
       return self.deathCondition
    
    def set_death_conditions(self, conditions:list):
        self.deathCondition = conditions
    
    def update_death_conditions(self, lowerLimit, higherLimit=9):
        self.deathCondition = [n for n in range(0, lowerLimit+1)] +([n for n in range(higherLimit,9)] if higherLimit<9 else [])
    
    def draw(self,surf):
        draw.rect(surf, self.life_colour if self.get_state() else self.death_colour, self.rect)
        draw.rect(surf, self.life_colour if self.get_new_state() else self.death_colour, self.next_indicator)
        
    def update(self, event_list):
        #automatically update state
        self.state = self.get_new_state()
        self.update_new_state()

    def __str__(self):
        return 'X' if self.get_state() else '.'