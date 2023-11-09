import mesa
from car_model import CarModel

def agent_portrayal(agent):
    portrayal = {"Shape": "rect",
                 "Color": "blue",
                 "Filled": "true",
                 "Layer": 0,
                 "w": 1,
                 "h": 1}

    return portrayal

model_params = {
    "width": 20,
    "height": 20,
    "num_cars": 4,
    "num_intersecting": 4,
}

grid = mesa.visualization.CanvasGrid(agent_portrayal, model_params["width"], model_params["height"], 500, 500)

chart = mesa.visualization.ChartModule([{"Label": "Número de agentes", "Color": "red"}])

server = mesa.visualization.ModularServer(CarModel,
                       [grid, chart],
                       "Car Model",
                       model_params)
