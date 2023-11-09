import mesa

class CarAgent(mesa.Agent):
    """
    Moving upward car agent
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.crashed = False  # Inicializamos la variable "chocado" como False

    def step(self):
        if not self.crashed:
            self.model.grid.move_agent(self, (self.pos[0], self.pos[1] + 1))

class IntersectingCarAgent(mesa.Agent):
    """
    Moving rightward car agent
    """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.crashed = False  # Inicializamos la variable "chocado" como False

    def step(self):
        if not self.crashed:
            self.model.grid.move_agent(self, (self.pos[0] + 1, self.pos[1]))

class CarModel(mesa.Model):
    """
    Model class for the CarModel.
    """
    def __init__(self, width, height, num_cars, num_intersecting):
        self.num_cars = num_cars
        self.num_intersecting= num_intersecting
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)

        # Crear agentes CarModel
        for i in range(self.num_cars):
            agent = CarAgent(i, self)
            x = i + 9
            y = self.random.randrange(3)
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)

        # Crear agentes intersecciones
        for i in range(self.num_intersecting):
            agent = IntersectingCarAgent(i+4, self)
            x = self.random.randrange(3)
            y = i + 9
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)


        # DataCollector para recopilar información (opcional)
        self.datacollector = mesa.DataCollector()

    def step(self):
        # Avanzar en un paso de tiempo
        self.schedule.step()
        # Recopilar datos (opcional)
        self.datacollector.collect(self)
