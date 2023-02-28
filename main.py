import datetime
import calendar

class Employee:
    raise_amount = 1.04
    num_emps = 0
    # This is the constructor. Self is the instance of the class e.g. emp_1 is the instance
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.date = datetime.datetime.now()
        self.email = first + "." + last + "@company.com"
        # Each time an instance is instantiated 1 is added to this variable
        # This does not use self as it doesn't need to change based on an instance
        Employee.num_emps += 1

    # Method requires self as an argument in order to reference class attributes
    # Self allows the method to take in the instance on which it is called i.e, emp1.method()
    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        return self.salary * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Class methods can also be used as alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        salary = int(salary)
        return cls(first, last, salary)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            day = calendar.day_name[day.weekday()]
            return False, day
        day = calendar.day_name[day.weekday()]
        return True, day







print(f"Number of employees: {Employee.num_emps}")
emp_1 = Employee('John', 'Molesworth', 50000)
emp_2 = Employee('Barry', 'Barnes', 50000)
print(f"Number of employees: {Employee.num_emps}")
# Here the method full_name is being called on emp_1 so there is no need to pass
# the argument as self handles that
print(emp_1.full_name())
# Here the method full_name is being called on the class Employee so needs an argument
# of emp_1 to be provided
print(Employee.full_name(emp_1))
print(emp_1.date)
print(emp_2.date)
print(emp_1.salary)
print(emp_1.apply_raise())
print(emp_1.raise_amount)
# Set a class variable only on a particular instance of that class
emp_1.raise_amount = 33
print(emp_1.raise_amount)
print(emp_1.apply_raise())

# Set a class variable across entire class except for the above that was individually specified
Employee.raise_amount = 14
print(emp_1.raise_amount)
print(emp_1.apply_raise())
print(emp_2.raise_amount)
print(emp_2.apply_raise())


# Using class method cls. to take a string and split it into usable variables to make an Employee object
emp_str_1 = 'John-Molesworth-52000'
new_emp = Employee.from_string(emp_str_1)
print(new_emp.first)
print(new_emp.last)
print(new_emp.full_name())
print(new_emp.email)
print("Before salary", new_emp.salary)
Employee.apply_raise(new_emp)
new_emp.salary = new_emp.apply_raise()
print(type(new_emp.salary))
print("After salary", new_emp.salary)
print(new_emp.raise_amount)


new_emp2 = Employee('Jimmy', 'Junior', 12000)
print(new_emp2.full_name())
print(new_emp2.salary)
new_emp2.salary = new_emp2.apply_raise()
print(new_emp2.salary)

my_date = datetime.date(2023, 2, 25)
print(Employee.is_weekday(my_date))