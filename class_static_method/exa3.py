class Employee:
    NO_OF_EMPLOYEES = 0
  
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increment_employees()
    def give_raise(self, amount):
        self.salary += amount
    @classmethod
    def employee_from_full_name(cls, full_name, salary):
        split_name = full_name.split(' ')
        first_name = split_name[0]
        last_name = split_name[1]
        return cls(first_name, last_name, salary)
    @classmethod
    def increment_employees(cls):
        cls.NO_OF_EMPLOYEES += 1
    @staticmethod
    def get_employee_legal_obligations_txt():
        legal_obligations = """
        1. An employee must complete 8 hours per working day
        2. ...
        """
        return legal_obligations

employee_1 = Employee('Andrew', 'Brown', 85000)
print(employee_1.first_name)
print(employee_1.salary)
print(Employee.get_employee_legal_obligations_txt())

