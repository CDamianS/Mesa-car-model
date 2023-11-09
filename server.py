import mesa
from car_model import CarModel, CarAgent, IntersectingCarAgent

def agent_portrayal(agent):
    portrayal = {"Shape": "rect",
                 "Color": "blue",
                 "Filled": "true",
                 "Layer": 0,
                 "w": 1,
                 "h": 1}

    if isinstance(agent, CarAgent):
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
    else:
        portrayal["color"] = "blue"
        portrayal["Layer"] = 1

    return portrayal

model_params = {
    "width": 20,
    "height": 20,
    "num_cars": 2,
    "num_intersecting": 2,
}

grid = mesa.visualization.CanvasGrid(agent_portrayal, model_params["width"], model_params["height"], 500, 500)

chart = mesa.visualization.ChartModule([{"Label": "Número de agentes", "Color": "red"}])

server = mesa.visualization.ModularServer(CarModel,
                       [grid, chart],
                       "Car Model",
                       model_params)
