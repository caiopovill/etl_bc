from typing import Dict
from abc import ABC, abstractmethod

class DatabaseRepositoryIntarface(ABC):

    @abstractmethod
    def insert_artist(self, data: Dict) -> None:
        pass
    