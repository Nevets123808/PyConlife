class Cell():
    state: bool = False
    neighbours: list = []
    newState: bool = False
    birthCondition:list = []
    deathCondition:list = []
    
    def __init__(self, state=False, neighbours:list = [], birthCondition = [3,4], deathCondition = [2,6]):
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
    
    def __str__(self):
        return 'X' if self.get_state() else '.'