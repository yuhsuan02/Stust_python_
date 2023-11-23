class Employee:
    def __init__(emp, name,id, salary,department,hours_worked):
        emp.name = name
        emp.id=id
        emp.department = department
        emp.salary = salary
        emp.hours_worked=hours_worked
    def print_employee_details(emp):
        print("My name is {}\nId is {}\nSalary is {}\nDepartment is {}\nhours_worked is {}".format(emp.name,emp.id,emp.salary,emp.department,emp.hours_worked))      

    def calculate_emp_salary(emp):
        overtime = emp.hours_worked - 50
        overtimeamount = (overtime * (emp.salary / 50))
        print("overtime pay ",overtimeamount)  
        print("\n")

    def assign_department(emp,newdepartment):
        emp.department=newdepartment

# Corrected object instantiation
obj1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING",60 )
obj2 = Employee("JONES", "E7499", 45000, "RESEARCH",50 )
obj3 = Employee("MARTIN", "E7900", 50000, "SALES",55)
obj4 = Employee("SMITH", "E7698", 55000, "OPERATIONS",53)

# Calling the talk method using the object instances
obj1.assign_department("SALES")
obj1.print_employee_details()
obj1.calculate_emp_salary()
obj2.print_employee_details()
obj2.calculate_emp_salary()
obj3.print_employee_details()
obj3.calculate_emp_salary()
obj4.print_employee_details()
obj4.calculate_emp_salary()