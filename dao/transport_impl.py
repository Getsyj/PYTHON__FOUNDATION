import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.transport_service import TransportService
from entity.vehicle   import Vehicle
from entity.driver    import Driver
from entity.booking   import Booking
from util.db_conn_util import get_connection

from exception.booking_not_found_exception import BookingNotFoundException
from exception.vehicle_not_found_exception  import VehicleNotFoundException


class TransportServiceImpl(TransportService):
  
    def add_vehicle(self, vehicle: Vehicle) -> bool:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (%s, %s, %s, %s)",
                (vehicle.model, vehicle.capacity, vehicle.vehicle_type, vehicle.status)
            )
            conn.commit()
            return True
        except Exception as e:
            print("Error in add_vehicle:", e)
            return False
        finally:
            cursor.close(); conn.close()

    def update_vehicle(self, vehicle: Vehicle) -> bool:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute(
                "UPDATE Vehicles SET Model=%s, Capacity=%s, Type=%s, Status=%s WHERE VehicleID=%s",
                (vehicle.model, vehicle.capacity, vehicle.vehicle_type,
                 vehicle.status, vehicle.vehicle_id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(" Error in update_vehicle:", e)
            return False
        finally:
            cursor.close(); conn.close()

    def delete_vehicle(self, vehicle_id: int) -> bool:
        """
        Safe delete: prevent deletion while trips still reference the vehicle.
        """
        try:
            conn = get_connection(); cursor = conn.cursor()

          
            cursor.execute("SELECT COUNT(*) FROM Trips WHERE VehicleID = %s", (vehicle_id,))
            (ref_count,) = cursor.fetchone()
            if ref_count > 0:
                print(f" Cannot delete vehicle {vehicle_id}: referenced by {ref_count} trip(s).")
                return False

         
            cursor.execute("DELETE FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise VehicleNotFoundException(vehicle_id)
            return True

        except VehicleNotFoundException as ve:
            print(ve); return False
        except Exception as e:
            print(" Error in delete_vehicle:", e); return False
        finally:
            cursor.close(); conn.close()

    def get_all_vehicles(self) -> list[Vehicle]:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute("SELECT VehicleID, Model, Capacity, Type, Status FROM Vehicles")
            return [
                Vehicle(vehicle_id=r[0], model=r[1], capacity=r[2],
                        vehicle_type=r[3], status=r[4])
                for r in cursor.fetchall()
            ]
        except Exception as e:
            print(" Error in get_all_vehicles:", e)
            return []
        finally:
            cursor.close(); conn.close()

    
    def book_trip(self, trip_id: int, passenger_id: int, booking_date: str) -> bool:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status)"
                " VALUES (%s, %s, %s, 'Confirmed')",
                (trip_id, passenger_id, booking_date)
            )
            conn.commit(); return True
        except Exception as e:
            print(" Error in book_trip:", e); return False
        finally:
            cursor.close(); conn.close()

    def cancel_booking(self, booking_id: int) -> bool:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute("UPDATE Bookings SET Status='Cancelled' WHERE BookingID=%s",
                           (booking_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise BookingNotFoundException(booking_id)
            return True
        except BookingNotFoundException as be:
            print(be); return False
        except Exception as e:
            print(" Error in cancel_booking:", e); return False
        finally:
            cursor.close(); conn.close()

    def get_bookings_by_passenger(self, passenger_id: int) -> list[Booking]:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute(
                "SELECT BookingID, TripID, PassengerID, BookingDate, Status "
                "FROM Bookings WHERE PassengerID=%s", (passenger_id,)
            )
            return [Booking(*r) for r in cursor.fetchall()]
        except Exception as e:
            print(" Error in get_bookings_by_passenger:", e); return []
        finally:
            cursor.close(); conn.close()

    def get_bookings_by_trip(self, trip_id: int) -> list[Booking]:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute(
                "SELECT BookingID, TripID, PassengerID, BookingDate, Status "
                "FROM Bookings WHERE TripID=%s", (trip_id,)
            )
            return [Booking(*r) for r in cursor.fetchall()]
        except Exception as e:
            print(" Error in get_bookings_by_trip:", e); return []
        finally:
            cursor.close(); conn.close()

  
    def get_available_drivers(self) -> list[Driver]:
        try:
            conn = get_connection(); cursor = conn.cursor()
            cursor.execute("""
                SELECT DriverID, Name, LicenseNumber, Status
                FROM Drivers
                WHERE DriverID NOT IN (
                    SELECT DISTINCT IFNULL(DriverID, 0)
                    FROM Trips
                    WHERE Status IN ('Scheduled', 'Ongoing')
                )
            """)
            return [
                Driver(
                    driver_id=r[0],
                    name=r[1],
                    license_number=r[2],
                    contact_number=None,
                    status=r[3]
                )
                for r in cursor.fetchall()
            ]
        except Exception as e:
            print(" Error in get_available_drivers:", e)
            return []
        finally:
            cursor.close(); conn.close()

