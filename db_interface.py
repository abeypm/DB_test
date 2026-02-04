from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
        
    @abstractmethod
    def execute(self, query: str, params=None):
        pass

    @abstractmethod
    def create(self, table: str, data: Dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def read(self, table: str, criteria: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def update(self, table: str, criteria: Dict[str, Any], data: Dict[str, Any]) -> int:
        pass

    @abstractmethod
    def delete(self, table: str, criteria: Dict[str, Any]) -> int:
        pass

    @abstractmethod
    def close(self):
        pass
