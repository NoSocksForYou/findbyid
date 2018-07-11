import random

class FindByIDFactory:
    used_ids = [] # Required for the getFreeID function to work properly.

    def __init__(self, *args, **kwargs):
        cls = type(self)
        if not hasattr(cls, "has_instantiated"):
            cls.instances = []
            cls.has_instantiated = True

        self.ID = cls.getFreeID()
        cls.instances.append(self)

    @classmethod
    def getFreeID(cls):
        while True:
            id = random.randint(10000, 100000)
            if id not in cls.used_ids:
                break

        return id

    @classmethod
    def findByID(cls, ID):

        for i in cls.instances:
            if i.ID == ID:
                return i
        else:
            raise Exception("Invalid ID!")

    @classmethod
    def getInstances(cls):
        return cls.instances


