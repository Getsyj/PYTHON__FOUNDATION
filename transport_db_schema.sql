
CREATE DATABASE transport_db;
USE transport_db;

CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    Model VARCHAR(255),
    Capacity DECIMAL(10,2),
    Type VARCHAR(50),
    Status VARCHAR(50)
);

CREATE TABLE Routes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,
    StartLocation VARCHAR(255),
    EndLocation VARCHAR(255),
    Distance DECIMAL(10,2)
);

CREATE TABLE Drivers (
    DriverID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    LicenseNumber VARCHAR(50) UNIQUE,
    Status VARCHAR(50)
);

CREATE TABLE Passengers (
    PassengerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255),
    Gender VARCHAR(50),
    Age INT,
    Email VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(50)
);


CREATE TABLE Trips (
    TripID INT AUTO_INCREMENT PRIMARY KEY,
    VehicleID INT,
    RouteID INT,
    DriverID INT,
    DepartureDate DATE,
    ArrivalDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (RouteID)  REFERENCES Routes(RouteID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    TripID INT,
    PassengerID INT,
    BookingDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (TripID)      REFERENCES Trips(TripID),
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID)
);




INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES
('Tata Ace',              800.50,  'Car', 'Available'),
('Volvo 9700',              50.00, 'Bus', 'On Trip'),
('Ashok Leyland Dost',    1250.75, 'Van', 'Maintenance'),
('Eicher Pro 2049',       2000.00, 'Car', 'Available'),
('Scania Multi-Axle',       55.00, 'Bus', 'Available'),
('Mahindra Bolero Pik-Up', 900.00, 'Car', 'Available'),
('Force Traveller 3350',    15.00, 'Van', 'On Trip'),
('Isuzu N-Series',       1500.00, 'Car', 'Maintenance'),
('Mercedes-Benz Tourismo',  48.00, 'Bus', 'Available'),
('Ashok Leyland Boss',   1600.00, 'Car', 'Available');


INSERT INTO Routes (StartLocation, EndLocation, Distance) VALUES
('Chennai',   'Bengaluru', 350.00),
('Hyderabad', 'Vijayawada',275.50),
('Mumbai',    'Pune',      160.25),
('Delhi',     'Agra',      233.40),
('Kolkata',   'Durgapur',  180.75),
('Jaipur',    'Jodhpur',   337.60),
('Lucknow',   'Kanpur',     82.40),
('Ahmedabad', 'Surat',     265.30),
('Indore',    'Bhopal',    194.20),
('Trivandrum','Kochi',     205.10);


INSERT INTO Drivers (Name, LicenseNumber, Status) VALUES
('Rajesh Kumar', 'DL123456789', 'Available'),
('Vijay Sharma', 'DL987654321', 'Available'),
('Ramesh Patel', 'DL555666777', 'Available'),
('Nikhil Mehta', 'LIC-99988',   'Available'),
('Sneha Iyer',   'LIC-66221',   'Available'),
('Arjun Kapoor', 'LIC-77755',   'On Trip'),
('Rahul Bose',   'LIC-22334',   'On Trip'),
('Priya Nair',   'LIC-88990',   'On Trip'),
('Karan Gill',   'LIC-33221',   'Maintenance'),
('Meera Das',    'LIC-44455',   'Maintenance');

INSERT INTO Passengers (FirstName, Gender, Age, Email, PhoneNumber) VALUES
('Anita',  'Female', 25, 'anita@example.com',  '9876543210'),
('Rahul',  'Male',   30, 'rahul@example.com',  '9123456789'),
('Priya',  'Female', 22, 'priya@example.com',  '9012345678'),
('Arjun',  'Male',   28, 'arjun@example.com',  '9098765432'),
('Sneha',  'Female', 35, 'sneha@example.com',  '9988776655'),
('Deepak', 'Male',   27, 'deepak@example.com', '9998887776'),
('Ritu',   'Female', 26, 'ritu@example.com',   '8887776665'),
('Gaurav', 'Male',   32, 'gaurav@example.com', '7776665554'),
('Neha',   'Female', 24, 'neha@example.com',   '6665554443'),
('Amit',   'Male',   29, 'amit@example.com',   '5554443332');


INSERT INTO Trips (VehicleID, RouteID, DriverID, DepartureDate, ArrivalDate, Status) VALUES
(1, 1,  6, '2025-07-10', '2025-07-10', 'Scheduled'),
(2, 2,  1, '2025-07-11', '2025-07-11', 'Scheduled'),
(3, 3,  2, '2025-07-12', '2025-07-12', 'Ongoing'),
(4, 4,  3, '2025-07-13', '2025-07-13', 'Completed'),
(5, 5, NULL,'2025-07-14', '2025-07-14', 'Scheduled'),
(6, 6, NULL,'2025-07-15', '2025-07-15', 'Scheduled'),
(7, 7,  7, '2025-07-16', '2025-07-16', 'Ongoing'),
(8, 8,  8, '2025-07-17', '2025-07-17', 'Scheduled'),
(9, 9, NULL,'2025-07-18', '2025-07-18', 'Scheduled'),
(10,10, 4, '2025-07-19', '2025-07-19', 'Cancelled');


INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status) VALUES
(2,  1, '2025-07-08', 'Confirmed'),
(2,  2, '2025-07-08', 'Confirmed'),
(5,  3, '2025-07-12', 'Cancelled'),
(5,  4, '2025-07-12', 'Confirmed'),
(5,  5, '2025-07-12', 'Confirmed'),
(6,  6, '2025-07-13', 'Confirmed'),
(7,  7, '2025-07-14', 'Confirmed'),
(8,  8, '2025-07-15', 'Confirmed'),
(9,  9, '2025-07-16', 'Confirmed'),
(10,10, '2025-07-17', 'Cancelled');

UPDATE Vehicles SET Type = 'Car' WHERE Type = 'Truck';
SELECT * FROM Vehicles;


