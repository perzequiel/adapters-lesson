from typing import List
from domain.port import TaskPort
from domain.entity import TaskEntity

# datos de prueba
data = [
    ["1", "daily", "hacer una daily con el equipo"],
    ["2", "comprar", "hacer las compras en el chino"],
    ["3", "pasear", "caminar 5 km"],
    ["4", "almorzar", "calentar comida de anoche"],
    ["5", "siesta", "tirarse en el sillon un rato"],
    ["6", "peluqueria", "cortarse el pelo pero no mucho"],
]
# popular json de pruebas
tasks = [ { "id": d[0], "name": d[1], "description": d[2] } for d in data] 

class TaskRepoPostgreSQL(TaskPort):
    def __init__(self):
        # esto es para testear
        self.tasks = tasks

    def createTask(self, name: str, description: str) -> TaskEntity:
        ### simular postgres create
        new_id = len(self.tasks) + 1
        new_task = {"id": str(new_id), "name": name, "description": description}
        self.tasks.append(new_task)
        ###
        return TaskPort.create(new_task["id"], new_task["name"], new_task["description"])


    def getAllTask(self) -> List[TaskEntity]:
        ### implementacion de postgrsql
        # tasks = get all de postgresql
        tasks = self.tasks
        ## 
        return [ TaskPort.create(t["id"], t["name"], t["description"]) for t in tasks]