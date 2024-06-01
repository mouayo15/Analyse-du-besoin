from abc import ABC, abstractmethod

class ILecteur(ABC):
    @property
    @abstractmethod
    def badge_detecte(self):
        pass
