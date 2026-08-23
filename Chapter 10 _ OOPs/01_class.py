class Employee:   # this a class
    name= "nomi"   # these are class attributes
    language = "Py"
    salary = 24000


nomi = Employee()   # this is an object , here nomi is an object 
print(nomi.name,nomi.language,nomi.salary)

fawad = Employee()  # another object 
fawad.name = "Fawad ff"   # this is an object/instance attribute
print(fawad.name,fawad.language,fawad.salary)
# here name is object attribute and languange and salary are class attributes as they belongs to class
