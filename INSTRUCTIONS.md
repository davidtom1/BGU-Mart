# BGU Mart - Usage Instructions

## Setup and Installation

### Prerequisites
- Python 3.x installed on your system
- SQLite3 (comes bundled with Python)

### Initial Setup
No additional dependencies or installation required. The project uses only Python standard libraries.

## Running the System

### Step 1: Initialize the Database

Run the initialization script to create and populate the database:

```bash
python initiate.py config.txt
```

This will:
1. Delete any existing `bgumart.db` file
2. Create a new database with the proper schema
3. Populate the database with initial data from `config.txt`

**Expected Output**: A new `bgumart.db` file will be created in the project directory.

### Step 2: Process Activities

After initialization, process inventory activities:

```bash
python action.py action.txt
```

This will:
1. Read activities from the action file
2. Update product quantities based on activities
3. Record all activities in the activities table

**Activity Types**:
- Positive quantities: Restocking (from suppliers)
- Negative quantities: Sales (by employees)

**Validation**: The system prevents sales that would result in negative inventory.

### Step 3: View Database Contents

Use the printdb script to query the database:

```bash
python printdb.py
```

Note: This script needs to be implemented based on your reporting requirements.

## Input File Formats

### config.txt Format

The configuration file uses comma-separated values with a type prefix:

```
B,branch_id,location,number_of_employees
E,employee_id,name,salary,branch_id
S,supplier_id,name,contact_info
P,product_id,description,price,quantity
```

**Example**:
```
B,1,New York,50
E,101,John Smith,50000,1
S,1,Acme Inc.,(123) 456-7890
P,1,Apple,0.5,10
```

**Type Codes**:
- `B`: Branch
- `E`: Employee
- `S`: Supplier
- `P`: Product

### action.txt Format

Activities file format (no type prefix):

```
product_id, quantity, activator_id, date
```

**Example**:
```
3, 100, 1, 20230101
3, -20, 103, 20230201
```

**Fields**:
- `product_id`: ID of the product being restocked or sold
- `quantity`: Positive for restocking, negative for sales
- `activator_id`: Supplier ID (positive qty) or Employee ID (negative qty)
- `date`: Activity date in YYYYMMDD format

## Common Tasks

### Add New Data

To add new entities to the database:

1. Edit `config.txt` with new entries
2. Re-run `python initiate.py config.txt`

Warning: This will reset the entire database!

### Record New Activities

To record new inventory activities:

1. Edit `action.txt` with new activity entries
2. Run `python action.py action.txt`

### Query the Database

You can use SQLite command line or implement custom queries in `printdb.py`:

```bash
sqlite3 bgumart.db
```

**Example queries**:
```sql
SELECT * FROM products;
SELECT * FROM activities WHERE date = '20230101';
SELECT p.description, p.quantity FROM products p WHERE p.quantity < 10;
```

## Workflow Example

Complete workflow from scratch:

```bash
# 1. Initialize database
python initiate.py config.txt

# 2. Process initial activities
python action.py action.txt

# 3. View results
python printdb.py
# or use SQLite directly
sqlite3 bgumart.db "SELECT * FROM products;"
```

## Error Handling

### Common Issues

**Database locked error**:
- Close any SQLite database viewers
- Ensure no other Python processes are accessing the database

**File not found**:
- Verify config.txt and action.txt exist in the project directory
- Use correct relative or absolute paths

**Invalid quantity error**:
- Check that sales don't exceed available inventory
- Verify quantity values are integers

**Foreign key violations**:
- Ensure branches exist before adding employees
- Verify product and activator IDs exist before recording activities

## Extending the System

### Adding New Entity Types

1. Add DTO class in `persistence.py`
2. Add CREATE TABLE statement in `create_tables()`
3. Add parser function in `initiate.py`
4. Update `adders` dictionary with new type code

### Custom Queries

Implement report functions in `printdb.py` using:
```python
from persistence import repo

# Example: Get all products with low inventory
results = repo.execute_command("""
    SELECT description, quantity
    FROM products
    WHERE quantity < 20
""")
```

## Notes

- The database is automatically committed and closed on program exit
- All dates should use YYYYMMDD format for consistency
- IDs are managed manually; ensure uniqueness in config files
- The system uses a singleton repository pattern for database access
