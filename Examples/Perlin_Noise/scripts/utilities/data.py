class Data:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
    
    def load(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)