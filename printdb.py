from persistence import *

def main():
    print ("Activities")
    activities = repo.execute_command("""
        SELECT * FROM activities
        ORDER BY date
    """)
    for activitie in activities:
        print(activitie)
        
    print ("Branches")
    branches = repo.execute_command("""
        SELECT * FROM branches
        ORDER BY id
    """)
    for branche in branches:
        print (branche)
        
    print ("Employees")
    employees = repo.execute_command("""
        SELECT * FROM employees
        ORDER BY id
    """)
    for employee in employees:
        print(employee)
        
    print ("\nProducts")
    products = repo.execute_command("""
        SELECT * FROM products
        ORDER BY id
    """)
    for product in products:
        print(product)
        
    print ("\nSuppliers")
    suppliers = repo.execute_command("""
        SELECT * FROM suppliers
        ORDER BY id
    """)
    for supplier in suppliers:
        print(supplier)
        
    print ("\nEmployees report")
    employee_report = repo.execute_command("""
        SELECT 
            emp.name,
            emp.salary,
            b.location,
            COALESCE(SUM(CASE 
                WHEN a.quantity < 0 
                THEN -a.quantity * p.price 
                ELSE 0 
            END), 0) as total_sales_income
        FROM employees emp
        JOIN branches b ON emp.branche = b.id
        LEFT JOIN activities a ON emp.id = a.activator_id
        LEFT JOIN products p ON a.product_id = p.id
        GROUP BY emp.id
        ORDER BY emp.name
    """)
    for report in employee_report:
        print(f"{report[0]} {report[1]} {report[2]} {report[3]}")
        
    print("\nActivities report")
    activities_exist = repo.execute_command("""
        SELECT COUNT(*) FROM activities
    """)[0][0]
    
    if activities_exist > 0:
        activity_report = repo.execute_command("""
            SELECT 
                ac.date,
                p.description,
                ac.quantity,
                CASE 
                    WHEN ac.quantity < 0 THEN e.name 
                    ELSE 'None' 
                END as seller,
                CASE 
                    WHEN ac.quantity > 0 THEN s.name 
                    ELSE 'None' 
                END as supplier
            FROM activities ac
            JOIN products p ON ac.product_id = p.id
            LEFT JOIN employees e ON ac.activator_id = e.id
            LEFT JOIN suppliers s ON ac.activator_id = s.id
            ORDER BY ac.date
        """)
        for report in activity_report:
            print(report)
    

if __name__ == '__main__':
    main()