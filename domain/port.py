from abc import ABC, abstractmethod
from typing import List
from .entity import TaskEntity

class TaskPort(ABC):
    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    @abstractmethod
    def createTask(self, name: str, description: str) -> TaskEntity:
        """
        Docstring for createTask
        
        :param name: Description
        :type name: str
        :param description: Description
        :type description: str
        """
        pass
        
    @abstractmethod
    def getAllTask(self) -> List[TaskEntity]:
        """
        Docstring for getAllTask
        """
        pass

    @staticmethod
    def create(id: str, name: str, description: str):
        """
        Docstring for create
        
        :param id: Description
        :type id: str
        :param name: Description
        :type name: str
        :param description: Description
        :type description: str
        """
        return TaskEntity(id=id, name=name, description=description)
