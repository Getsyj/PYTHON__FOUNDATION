from dao.passenger_service import PassengerService
from entity.passenger import Passenger
from util.db_conn_util import get_connection

from exception.passenger_not_found_exception import PassengerNotFoundException


class PassengerServiceImpl(PassengerService):
 
    def add_passenger(self, passenger: Passenger) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Passengers (FirstName, Age, Gender, Email, PhoneNumber)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    passenger.first_name,
                    passenger.age,
                    passenger.gender,
                    passenger.email,
                    passenger.phone_number,
                ),
            )
            conn.commit()
            return True
        except Exception as e:
            print("❌ Error in add_passenger:", e)
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def get_all_passengers(self) -> list[Passenger]:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT PassengerID, FirstName, Age, Gender, Email, PhoneNumber
                FROM Passengers
                """
            )
            return [Passenger(*row) for row in cursor.fetchall()]
        except Exception as e:
            print("❌ Error in get_all_passengers:", e)
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def get_bookings_by_passenger(self, passenger_id: int) -> list:
        """
        Return all bookings for a given passenger.
        Raises PassengerNotFoundException if no bookings (or passenger) found.
        """
        bookings: list = []
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT BookingID, TripID, PassengerID, BookingDate, Status
                FROM Bookings
                WHERE PassengerID = %s
                """,
                (passenger_id,),
            )
            rows = cursor.fetchall()

            
            if not rows:
                raise PassengerNotFoundException(passenger_id)

            
            for row in rows:
                bookings.append(
                    {
                        "BookingID": row[0],
                        "TripID": row[1],
                        "PassengerID": row[2],
                        "BookingDate": str(row[3]),
                        "Status": row[4],
                    }
                )
                

        except PassengerNotFoundException as pe:
            print(pe)
        except Exception as e:
            print("❌ Error in get_bookings_by_passenger:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return bookings
