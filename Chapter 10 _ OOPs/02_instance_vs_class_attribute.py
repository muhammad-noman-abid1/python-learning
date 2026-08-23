class Employee:   
    name= "nomi"   # these are class attributes
    language = "Py"
    salary = 24000


nomi = Employee()   # this is an object , here nomi is an object 
nomi.language = "javascript" # instance attribute will print out because instance attribute take preference over class attributes
print(nomi.name,nomi.language,nomi.salary)

