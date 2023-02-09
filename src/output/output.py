from abc import ABC, abstractmethod

from src.app import Results


class Output(ABC):
    @abstractmethod
    def write(self, results: list[Results]) -> None:
        pass
