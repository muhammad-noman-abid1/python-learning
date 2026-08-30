class Employee:
    salary = 50000
    increment = 35

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary ) -1)*100

e = Employee()
print(f"Congratulations! Your new salary is: {e.salaryAfterIncrement}")
e.salaryAfterIncrement = (int(input("Enter your  new salary to get the increment percentage: ")))
print(f"Increment percentage is: {e.increment}%")