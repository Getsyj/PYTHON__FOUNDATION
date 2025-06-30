from dao.booking_service import BookingService
from entity.booking import Booking
from util.db_conn_util import get_connection


class BookingServiceImpl(BookingService):
    
    def add_booking(self, booking: Booking) -> bool:
        return self.book_trip(
            booking.trip_id,
            booking.passenger_id,
            booking.booking_date,
            booking.status
        )

   
    def book_trip(
        self,
        trip_id: int,
        passenger_id: int,
        booking_date: str,
        status: str = "Confirmed",
    ) -> bool:
        """
        Insert a booking row. Returns True on success, False on failure.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

           
            cursor.execute(
                "SELECT COUNT(*) FROM Bookings WHERE TripID=%s AND PassengerID=%s",
                (trip_id, passenger_id),
            )
            (count,) = cursor.fetchone()
            if count > 0:
                print("⚠️  Passenger already booked on this trip.")
                return False

            cursor.execute(
                """
                INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status)
                VALUES (%s, %s, %s, %s)
                """,
                (trip_id, passenger_id, booking_date, status),
            )
            conn.commit()
            return True
        except Exception as e:
            print("❌ Error in book_trip:", e)
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def cancel_booking(self, booking_id: int) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Bookings SET Status='Cancelled' WHERE BookingID=%s",
                (booking_id,),
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("❌ Error in cancel_booking:", e)
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

   
    def get_all_bookings(self) -> list[Booking]:
        bookings: list[Booking] = []
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT BookingID, TripID, PassengerID, BookingDate, Status FROM Bookings"
            )
            for row in cursor.fetchall():
                bookings.append(Booking(*row))
            return bookings
        except Exception as e:
            print("❌ Error in get_all_bookings:", e)
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
