-- Create the database for the hostel system
CREATE DATABASE hostel_management;

-- Use the database
USE hostel_management;

-- Create the rooms table
CREATE TABLE rooms (
    room_id VARCHAR(10) PRIMARY KEY,
    room_type VARCHAR(45) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN NOT NULL DEFAULT TRUE  -- To indicate if the room is available
);

-- Insert sample data into the rooms table
INSERT INTO rooms VALUES ('r001', 'Single', 50.00, true);
INSERT INTO rooms VALUES ('r002', 'Double', 75.00, false);
INSERT INTO rooms VALUES ('r003', 'Suite', 120.00, true);

-- Select all records from the rooms table
SELECT * FROM rooms;
