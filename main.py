## como no tengo infra voy a llamar a los casos de uso desde el main

# importo adapter para inyectar en el caso de uso
from adapters.task_repo_postgresql import TaskRepoPostgreSQL
# importo caso de use suponiendo que estamos en la implementacion de la ruta de la api
from services.use_cases import GetAllTaskUseCase, CreateTaskUseCase
# solo para formatear un poco 
import pprint


## simulando un GET /tasks 
repo1 = TaskRepoPostgreSQL()
# se inyect el repo como dependencia / no acoplado al caso de uso
use_case1 = GetAllTaskUseCase(repo1)
listed = use_case1.execute()

print("\n\n\n\n-- TEST 1 --\n\n##########\n# getAll #\n##########\n")
pprint.pprint([vars(task) for task in listed])

## simulando un POST /task
repo2 = TaskRepoPostgreSQL() # tranquilamente podria ser otra base de datos
use_case2 = CreateTaskUseCase(repo2)
# print(use_case1.execute())
new_task = use_case2.execute("salir", "del agujero interior")

print("\n\n-- TEST 2 --\n\n##########\n# Create. #\n##########\n")
pprint.pprint(vars(new_task))
# esto solo para mostrar creado en la lista
nueva_lista = GetAllTaskUseCase(repo2).execute()

print("\n##########\n# getAll #\n##########\n")
pprint.pprint([vars(task) for task in nueva_lista])


