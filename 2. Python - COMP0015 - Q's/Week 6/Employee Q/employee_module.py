
###  This module defines a class that models an employee.
#

## An employee has a name and a salary. 
#
class Employee:
    
    DEFAULT_STARTING_SALARY = 10000
    INCREMENT = 1000
    ZERO = 0
    
    
    ## Constructs an Employee with a name and starting salary.
    #  @param employee_name the name of the employee.
    #
    def __init__(self, employee_name, employee_title, employee_hired):
            self.name = employee_name
            self.title = employee_title
            self.hired = employee_hired
            self.salary = Employee.DEFAULT_STARTING_SALARY
         
            
    ##    
    # @return string representation of object.
    #
    def __str__(self):
        #return "Name: " + self.name + ", salary: " + str(self.salary) + ", title" + str(self.title), + ", hired" + self.hired
        return 'Name: {} , Salary: {} ,  Title: {} , Job Status: {} '.format(self.name, self.salary, self.title, self.hired)

    ## name property allows get/set access to Employee's name value.
    #  name must not be whitespace else a ValueError is raised.
    #
    @property
    def name(self):
        #print( "I'm the getter")
        return self._name
    
    @name.setter
    def name(self, theName):
       #print ("I'm the setter")        
        if len(theName.strip()) != 0:
            self._name = theName
        else:
            raise ValueError("Invalid name: " + name)
        
        
    ## Own getter and setter for employee title
    # Done
    # 
    
    @property
    def title(self):
        return self._title 
            
        
    @title.setter
    def title(self, theTitle):
        if len(theTitle.strip()) > 4 and theTitle.isalpha():
            self._title = theTitle
            return self._title
        else:
            raise ValueError("Invalid Title: ")
        
        
    ## Own getter and setter for employee being hired 
    #
    #
    
    @property
    def hired(self):
        return self._hired
            
        
    @hired.setter
    def hired(self, theHired):
        if theHired == "y":
            self._hired = "Hired"
        elif theHired == "n":
            self._hired = "Fired"
        else:
            print("ERROR")
        
    

    ## salary property allows get/set access to Employee's salary.
    #  salary will be set to zero if there is an attempt to reduce
    #  it below zero.
    #
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salaryAmount):
        if salaryAmount >= 0:
            self._salary = salaryAmount
        else:
            self._salary = 0
    
    
    ## Promotes the employee by increasing the salary by INCREMENT.    
    #
    def promote(self):
        self.salary += Employee.INCREMENT

    
    ## Demotes the employee by decreasing the salary by INCREMENT.    
    #
    def demote(self):
        self.salary -= Employee.INCREMENT
    
    
    ##  Fire and hire function
    def fire(self):
        self.salary = Employee.ZERO
    def hire(self):
        self.salary = Employee.DEFAULT_STARTING_SALARY

         
    ## Raises the salary of the employee by the amount passed as a parameter.    
    # @param pay_rise the amount by which the the salary should be raised.
    #
    def raise_salary_by(self, pay_rise):
        if pay_rise > 0 :
            self.salary += pay_rise
        
        
    ## Determines if this employee is equal to another employee.
    #  @param rhsValue the right-hand side employee.
    #  @return True if the names and the salaries are equal.
    #  @exception TypeError if the objects being compared are not
    #             the same type.
    #            
    def __eq__(self, rhsValue) :
        if isinstance(rhsValue, Employee) :
            return (self.name == rhsValue.name and
              self.salary == rhsValue.salary)
        else:
            raise TypeError("Argument must be an Employee object.")