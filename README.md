# BGU Mart Database Management System

A Python-based database management system for managing a retail store's inventory, employees, suppliers, and branches using SQLite.

## Project Overview

BGU Mart is a database application that provides functionality to:
- Initialize and populate a SQLite database with store data
- Track products, suppliers, employees, and branches
- Record and process inventory activities (restocking and sales)
- Query and display database contents

## Project Structure

```
Assignment4/
├── action.py           # Process inventory activities from action file
├── action.txt          # Sample activities data
├── config.txt          # Initial configuration data
├── dbtools.py          # Database DAO layer with ORM functionality
├── initiate.py         # Database initialization script
├── persistence.py      # Data models and repository pattern
├── printdb.py          # Database query and display utility
└── bgumart.db          # SQLite database (generated)
```

## Database Schema

### Tables

- **branches**: Store branch information
  - id (INTEGER, PRIMARY KEY)
  - location (TEXT)
  - number_of_employees (INTEGER)

- **employees**: Employee records
  - id (INTEGER, PRIMARY KEY)
  - name (TEXT)
  - salary (REAL)
  - branche (INTEGER, FOREIGN KEY)

- **suppliers**: Supplier information
  - id (INTEGER, PRIMARY KEY)
  - name (TEXT)
  - contact_information (TEXT)

- **products**: Product inventory
  - id (INTEGER, PRIMARY KEY)
  - description (TEXT)
  - price (REAL)
  - quantity (INTEGER)

- **activities**: Inventory activity log
  - product_id (INTEGER, FOREIGN KEY)
  - quantity (INTEGER)
  - activator_id (INTEGER)
  - date (TEXT)

## Components

### persistence.py
Defines data models (DTOs) and the Repository singleton pattern:
- `Employee`, `Supplier`, `Product`, `Branche`, `Activitie` classes
- `Repository` class managing database connection and DAOs
- Creates and manages SQLite database tables

### dbtools.py
Provides a generic DAO (Data Access Object) layer:
- Object-Relational Mapping (ORM) functionality
- CRUD operations: `insert()`, `find()`, `find_all()`, `delete()`
- Automatic SQL generation based on DTO classes

### initiate.py
Database initialization script:
- Deletes existing database if present
- Creates fresh database with schema
- Populates tables from configuration file
- Parses config.txt with format: `TYPE,field1,field2,...`

### action.py
Processes inventory activities:
- Reads activities from action file
- Updates product quantities
- Records activities in database
- Validates sufficient inventory for sales (negative quantities)

### printdb.py
Database query utility (to be implemented):
- Display database contents
- Generate reports

## Requirements

- Python 3.x
- SQLite3 (included with Python)

## License

Educational project for Systems Programming course.
