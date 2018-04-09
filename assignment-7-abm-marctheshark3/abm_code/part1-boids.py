import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class MyAgent(Agent):
    def __init__(self, name, model):
        super().__init__(name,model)

    def step(self):
        print("() activated", name)
        #whatever else the agent does when activated

class MyModel(Model):
    def __init__(self, n_agents):
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(10,10,torus = True)
        for i in range(n_agents):
            a = MyAgent(i,self)
            self.schedule.add(a)
            coords = (random.randrange(0,10), random.randrange(0,10))
            self.grid.place_agent(a,coords)
    def step(self):
        self.schedule.step()

model = MyModel(5)
model.step()