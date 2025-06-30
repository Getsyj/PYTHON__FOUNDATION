from dao.driver_service import DriverService
from entity.driver import Driver
from util.db_conn_util import get_connection

class DriverServiceImpl(DriverService):

    def add_driver(self, driver: Driver) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO Drivers (Name, LicenseNumber, Status)
                VALUES (%s, %s, %s)
            """
            values = (driver.name, driver.license_number, driver.status)
            cursor.execute(query, values)
            conn.commit()
            return True
        except Exception as e:
            print(" Error in add_driver:", e)
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def get_all_drivers(self) -> list[Driver]:
        drivers = []
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT DriverID, Name, LicenseNumber, Status FROM Drivers"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                driver = Driver(
                    driver_id=row[0],
                    name=row[1],
                    license_number=row[2],
                    status=row[3]
                )
                drivers.append(driver)
            return drivers
        except Exception as e:
            print(" Error in get_all_drivers:", e)
            return []
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

    def get_available_drivers(self) -> list[Driver]:
        available = []
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                SELECT DriverID, Name, LicenseNumber, Status
                FROM Drivers
                WHERE Status = 'Available'
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                driver = Driver(
                    driver_id=row[0],
                    name=row[1],
                    license_number=row[2],
                    status=row[3]
                )
                available.append(driver)
            return available
        except Exception as e:
            print(" Error in get_available_drivers:", e)
            return []
        finally:
            if cursor: cursor.close()
            if conn: conn.close()

