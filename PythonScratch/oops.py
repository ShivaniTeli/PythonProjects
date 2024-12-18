class emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getsalary(self):
        print(self.salary)

print("Emp Info:")
empl = emp("Shivani",765438990)
print(empl.name)
empl.getsalary()
print("Emp Info:")
teli = emp("Harry",50000)
print(teli.name)
teli.getsalary()
