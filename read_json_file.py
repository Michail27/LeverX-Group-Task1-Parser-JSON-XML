import json
from abc import ABC, abstractmethod


class AbstractLoad(ABC):
    @staticmethod
    @abstractmethod
    def load_json(filename):
        pass


class JsonLoad(AbstractLoad):
    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as file:
            data = json.loads(file.read())
            return data
