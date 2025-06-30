from dao.route_service import RouteService
from entity.route import Route
from util.db_conn_util import get_connection

class RouteServiceImpl(RouteService):

    def add_route(self, route: Route) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO Routes (start_location, end_location, distance) VALUES (%s, %s, %s)"
            values = (route.start_location, route.end_location, route.distance)
            cursor.execute(query, values)
            conn.commit()
            return True
        except Exception as e:
            print(" Error in add_route:", e)
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def get_all_routes(self) -> list[Route]:
        routes = []
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT RouteID, start_location, end_location, distance FROM Routes"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                route = Route(*row)
                routes.append(route)
            return routes
        except Exception as e:
            print(" Error in get_all_routes:", e)
            return []
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
