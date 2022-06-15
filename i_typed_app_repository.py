# pylint: skip-file
# type: ignore

from abc import abstractmethod, ABC


class ITypedAppRepository(ABC):
    @abstractmethod
    def countAllResourceGroupByType(self):
        ...

    @abstractmethod
    def countEdgeGroupBySourceId(self):
        ...
