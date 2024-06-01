from abc import ABC, abstractmethod

class ILecteur(ABC):
    @abstractmethod
    def read(self):
        pass
