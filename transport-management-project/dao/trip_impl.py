from typing import List
from dao.trip_service import TripService
from entity.trip import Trip
from util.db_conn_util import get_connection
from exception.trip_not_found_exception import TripNotFoundException
from exception.driver_not_found_exception import DriverNotFoundException

class TripServiceImpl(TripService):
    def schedule_trip(self, trip: Trip) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Trips (VehicleID, RouteID, DriverID, DepartureDate, ArrivalDate, Status)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (trip.vehicle_id, trip.route_id, trip.driver_id, trip.departure_date, trip.arrival_date, trip.status),
            )
            conn.commit()
            return True
        except Exception as e:
            print("❌ Error in schedule_trip:", e)
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def cancel_trip(self, trip_id: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Trips SET Status = 'Cancelled' WHERE TripID = %s", (trip_id,))
            if cursor.rowcount == 0:
                raise TripNotFoundException(trip_id)
            conn.commit()
            return True
        except TripNotFoundException as te:
            print(te)
            return False
        except Exception as e:
            print("❌ Error in cancel_trip:", e)
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def allocate_driver_to_trip(self, trip_id: int, driver_id: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Trips SET DriverID = %s WHERE TripID = %s", (driver_id, trip_id))
            if cursor.rowcount == 0:
                raise DriverNotFoundException(driver_id)
            conn.commit()
            return True
        except DriverNotFoundException as de:
            print(de)
            return False
        except Exception as e:
            print("❌ Error in allocate_driver_to_trip:", e)
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def deallocate_driver(self, trip_id: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Trips SET DriverID = NULL WHERE TripID = %s", (trip_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("❌ Error in deallocate_driver:", e)
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def get_all_trips(self) -> List[Trip]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT TripID, VehicleID, RouteID, DriverID, DepartureDate, ArrivalDate, Status
                FROM Trips ORDER BY TripID
                """
            )
            rows = cursor.fetchall()
            return [Trip(*row) for row in rows]
        except Exception as e:
            print("❌ Error in get_all_trips:", e)
            return []
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def get_bookings_by_trip(self, trip_id: int) -> list:
        bookings = []
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT BookingID, TripID, PassengerID, BookingDate, Status
                FROM Bookings WHERE TripID = %s
                """,
                (trip_id,),
            )
            for row in cursor.fetchall():
                bookings.append({
                    "BookingID": row[0],
                    "TripID": row[1],
                    "PassengerID": row[2],
                    "BookingDate": str(row[3]),
                    "Status": row[4]
                })
        except Exception as e:
            print("❌ Error in get_bookings_by_trip:", e)
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
        return bookings

