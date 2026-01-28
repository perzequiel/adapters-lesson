from dataclasses import dataclass

@dataclass
class TaskEntity:
    id: str
    name: str
    description: str

    @staticmethod
    def create(id: str, name: str, description: str) -> 'TaskEntity':
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
    