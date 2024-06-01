from abc import ABC, abstractmethod

class IPorte(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
