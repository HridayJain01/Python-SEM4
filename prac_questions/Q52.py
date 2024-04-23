class Employee:
    def __init__(self,id,name,dept):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=0
        self.emp_department=dept
    

    def calsal(self):
        if(self.emp_department=="IT"):
            self.emp_salary="1000000"
        if(self.emp_department=="Comps"):
            self.emp_salary="2000000"
        if(self.emp_department=="AIDS"):
            self.emp_salary="1000000"
        return self.emp_salary
    
    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)
        
emp=Employee(0,"Hriday","IT")
print(emp.calsal())
emp.print_employee_details()
        
    

    

    
        
