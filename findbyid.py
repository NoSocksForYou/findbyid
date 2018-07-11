import random

class NotFoundException(Exception):
    pass

class FindByIDFactory:
    used_ids = [] # Required for the getFreeID function to work properly.

    def __init__(self, *args, **kwargs) -> None:
        cls = type(self)
        if not hasattr(cls, "has_instantiated_before"):
            cls.instances = []
            cls.has_instantiated = True

        self.ID = cls.__getFreeID()
        cls.instances.append(self)

    @classmethod
    def __getFreeID(cls) -> int:
        while True:
            id = random.randint(10000, 100000)
            if id not in cls.used_ids:
                break
        cls.used_ids.append(id)
        return id

    @classmethod
    def findByID(cls, ID: int) -> object:

        for i in cls.instances:
            if i.ID == ID:
                return i
        else:
            raise NotFoundException("Invalid ID!")

    @classmethod
    def getInstances(cls) -> list:
        return cls.instances

