from datetime import datetime

from dao.passenger_impl import PassengerServiceImpl
from dao.transport_impl import TransportServiceImpl
from dao.route_impl import RouteServiceImpl
from dao.driver_impl import DriverServiceImpl
from dao.trip_impl import TripServiceImpl
from dao.booking_impl import BookingServiceImpl

from entity.vehicle import Vehicle
from entity.trip import Trip

from exception.vehicle_not_found_exception import VehicleNotFoundException
from exception.booking_not_found_exception import BookingNotFoundException


class TransportManagementApp:
    @staticmethod
    def main() -> None:
       
        vehicle_service   = TransportServiceImpl()
        route_service     = RouteServiceImpl()
        passenger_service = PassengerServiceImpl()
        driver_service    = DriverServiceImpl()
        trip_service      = TripServiceImpl()
        booking_service   = BookingServiceImpl()

        #main
        while True:
            print("\n====== 🚚 Transport Management System ======")
            print("1.  Add Vehicle")
            print("2.  Update Vehicle")
            print("3.  Delete Vehicle")
            print("4.  Schedule Trip")
            print("5.  Cancel Trip")
            print("6.  Allocate Driver to Trip")
            print("7.  Deallocate Driver from Trip")
            print("8.  Book Trip for Passenger")
            print("9.  Cancel Booking")
            print("10. View Bookings by Passenger")
            print("11. View Bookings by Trip")
            print("12. View Available Drivers")
            print("-------------------------------------------")
            print("=== 📦 Additional Features ===")
            print("13. View All Vehicles")
            print("14. View All Drivers")
            print("15. View All Passengers")
            print("16. View All Trips")
            print("17. View All Bookings")
            print("0.  Exit")

            choice = input("Enter your choice: ").strip()

            # Add Vehicle
            if choice == '1':
                model        = input("Enter vehicle model: ")
                capacity     = float(input("Enter vehicle capacity: "))
                vehicle_type = input("Enter vehicle type (Bus/Car/Van): ")
                status       = input("Enter status (Available/On Trip/Maintenance): ")
                vehicle      = Vehicle(model=model, capacity=capacity,
                                        vehicle_type=vehicle_type, status=status)
                print("✅ Vehicle added successfully."
                      if vehicle_service.add_vehicle(vehicle)
                      else "❌ Failed to add vehicle.")

            # Update Vehicle
            elif choice == '2':
                vehicle_id   = int(input("Enter vehicle ID to update: "))
                model        = input("Enter new model: ")
                capacity     = float(input("Enter new capacity: "))
                vehicle_type = input("Enter new type (Bus/Car/Van): ")
                status       = input("Enter new status: ")
                vehicle      = Vehicle(vehicle_id=vehicle_id, model=model,
                                        capacity=capacity, vehicle_type=vehicle_type, status=status)
                print("✅ Vehicle updated!"
                      if vehicle_service.update_vehicle(vehicle)
                      else "❌ Update failed.")

            # Delete Vehicle
            elif choice == '3':
                try:
                    vehicle_id = int(input("Enter vehicle ID to delete: "))
                    success    = vehicle_service.delete_vehicle(vehicle_id)
                    print("✅ Vehicle deleted successfully." if success
                          else "❌ Vehicle could not be deleted.")
                except VehicleNotFoundException as ve:
                    print(ve)
                except ValueError:
                    print("❌ Invalid input – Vehicle ID must be a number.")
                except Exception as e:
                    print("❌ Unexpected error:", e)

            # Schedule Trip
            elif choice == '4':
                try:
                    vehicle_id    = int(input("Enter Vehicle ID: "))
                    route_id      = int(input("Enter Route ID: "))
                    driver_id     = int(input("Enter Driver ID: "))
                    dep_str       = input("Enter Departure Date (DD-MM-YYYY): ")
                    arr_str       = input("Enter Arrival Date (DD-MM-YYYY): ")
                    status        = input("Enter status (Scheduled/Ongoing/Completed/Cancelled): ")
                    departure_date = datetime.strptime(dep_str, '%d-%m-%Y').date()
                    arrival_date   = datetime.strptime(arr_str, '%d-%m-%Y').date()
                    trip = Trip(None, vehicle_id, route_id, driver_id,
                                departure_date, arrival_date, status)
                    print("✅ Trip scheduled successfully."
                          if trip_service.schedule_trip(trip)
                          else "❌ Failed to schedule trip.")
                except Exception as e:
                    print("❌ Invalid input:", e)

            # Cancel Trip
            elif choice == '5':
                try:
                    trip_id = int(input("Enter Trip ID to cancel: "))
                    print("✅ Trip cancelled successfully."
                          if trip_service.cancel_trip(trip_id)
                          else "❌ Failed to cancel trip.")
                except ValueError:
                    print("❌ Invalid Trip ID – must be a number.")

            # Allocate Driver
            elif choice == '6':
                try:
                    trip_id   = int(input("Enter Trip ID: "))
                    driver_id = int(input("Enter Driver ID to allocate: "))
                    success   = trip_service.allocate_driver_to_trip(trip_id, driver_id)
                    print("✅ Driver allocated successfully." if success
                          else "❌ Failed to allocate driver.")
                except ValueError:
                    print("❌ Trip ID and Driver ID must be numbers.")

            # Deallocate Driver
            elif choice == '7':
                try:
                    trip_id = int(input("Enter Trip ID: "))
                    success = trip_service.deallocate_driver(trip_id)
                    print("✅ Driver deallocated successfully." if success
                          else "❌ Failed to deallocate driver.")
                except ValueError:
                    print("❌ Trip ID must be a number.")

            #Book Trip for Passenger  (FIXED)
            elif choice == '8':
                try:
                    trip_id      = int(input("Enter Trip ID: "))
                    passenger_id = int(input("Enter Passenger ID: "))
                    date_str     = input("Enter Booking Date (DD-MM-YYYY): ").strip()
                    datetime.strptime(date_str, '%d-%m-%Y')   # validate
                    booking_date = datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
                    success = booking_service.book_trip(trip_id, passenger_id, booking_date)
                    print("✅ Booking confirmed successfully." if success
                          else "❌ Failed to confirm booking.")
                except ValueError:
                    print("❌ Date or numeric input invalid.")
                except Exception as e:
                    print("❌ Unexpected error while booking:", e)

            # Cancel Booking
            elif choice == '9':
                try:
                    booking_id = int(input("Enter Booking ID to cancel: "))
                    success    = vehicle_service.cancel_booking(booking_id)
                    print("✅ Booking cancelled successfully." if success
                          else "❌ Booking could not be cancelled.")
                except BookingNotFoundException as be:
                    print(be)
                except ValueError:
                    print("❌ Invalid Booking ID – must be a number.")
                except Exception as e:
                    print("❌ Unexpected error:", e)

            #View Bookings by Passenger
            elif choice == '10':
                try:
                    passenger_id = int(input("Enter Passenger ID to view bookings: "))
                    bookings     = passenger_service.get_bookings_by_passenger(passenger_id)
                    if bookings:
                        print("📄 Bookings for Passenger:")
                        for b in bookings:
                            print(b)
                    else:
                        print("⚠️  No bookings found for this passenger.")
                except ValueError:
                    print("❌ Passenger ID must be a number.")

            # View Bookings by Trip
            elif choice == '11':
                try:
                    trip_id  = int(input("Enter Trip ID to view bookings: "))
                    bookings = trip_service.get_bookings_by_trip(trip_id)
                    if bookings:
                        print("📄 Bookings for Trip:")
                        for b in bookings:
                            print(b)
                    else:
                        print("⚠️  No bookings found for this trip.")
                except ValueError:
                    print("❌ Trip ID must be a number.")

            # View Available Drivers
            elif choice == '12':
                drivers = driver_service.get_available_drivers()
                if drivers:
                    print("✅ Available Drivers:")
                    for d in drivers:
                        print(d)
                else:
                    print("⚠️  No drivers are currently available.")

            # View All Vehicles
            elif choice == '13':
                vehicles = vehicle_service.get_all_vehicles()
                if vehicles:
                    print("🚗 All Vehicles:")
                    for v in vehicles:
                        print(v)
                else:
                    print("⚠️  No vehicles found.")

            # View All Drivers
            elif choice == '14':
                drivers = driver_service.get_all_drivers()
                if drivers:
                    print("🧑‍✈️ All Drivers:")
                    for d in drivers:
                        print(d)
                else:
                    print("⚠️  No drivers found.")

            # View All Passengers
            elif choice == '15':
                passengers = passenger_service.get_all_passengers()
                if passengers:
                    print("🧍 All Passengers:")
                    for p in passengers:
                        print(p)
                else:
                    print("⚠️  No passengers found.")

            #View All Trips
            elif choice == '16':
                trips = trip_service.get_all_trips()
                if trips:
                    print("🚌 All Trips:")
                    for t in trips:
                        print(t)
                else:
                    print("⚠️  No trips found.")

            #View All Bookings
            elif choice == '17':
                bookings = booking_service.get_all_bookings()
                if bookings:
                    print("📑 All Bookings:")
                    for b in bookings:
                        print(b)
                else:
                    print("⚠️  No bookings found.")

            # Exit
            elif choice == '0':
                print("👋 Exiting the system. Goodbye!")
                break

            # Invalid Choice
            else:
                print("❌ Invalid choice. Please try again.")



if __name__ == "__main__":
    TransportManagementApp.main()
