class Programmer:
    company = "Google"
    def __init__(self, name, salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Nomi",500000, 1222)
print(p.name,p.salary,p.company, p.pin)
f = Programmer("Fawad",150000, 1212)
print(f.name,f.salary,f.company, f.pin)


