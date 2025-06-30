from abc import ABC, abstractmethod
from entity.route import Route

class RouteService(ABC):

    @abstractmethod
    def add_route(self, route: Route) -> bool:
        pass

    @abstractmethod
    def get_all_routes(self) -> list[Route]:
        pass
