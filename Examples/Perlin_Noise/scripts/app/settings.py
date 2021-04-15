from os.path import join

from scripts.utilities.filehandle import json_open, json_save

class Settings:
    def __init__(self, CONSTANTS):
        self.file = join(CONSTANTS.PATHS.EXEC, CONSTANTS.FILES.SETTINGS)

        self.attrs = []

        try:
            data = json_open(self.file)
        except FileNotFoundError:
            data = CONSTANTS.DEFAULT_SETTINGS
            json_save(self.file, data)

        for k,v in CONSTANTS.DEFAULT_SETTINGS.items():
            self.attrs.append(k)
            self.__setattr__(k,v)

        for k,v in data.items():
            if k not in self.attrs:
                self.attrs.append(k)
            self.__setattr__(k,v)

    def assign(self, key, value):
        if key not in self.attrs:
            self.attrs.append(key)
        self.__setattr__(key,value)

    def save(self):
        data = {}
        for attr in self.attrs:
            data[attr] = getattr(self, attr)
        json_save(self.file, data)