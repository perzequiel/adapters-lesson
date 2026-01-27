from domain.port import TaskPort

class CreateTaskUseCase:
    def __init__(self, repo: TaskPort):
        self.repo = repo
    
    def execute(self, name: str, description: str):
        task = self.repo.createTask(name, description)
        return task


class GetAllTaskUseCase:
    def __init__(self, repo: TaskPort):
        self.repo = repo

    def execute(self):
        return self.repo.getAllTask()
