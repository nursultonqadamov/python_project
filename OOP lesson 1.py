class Employee:
    def __init__(self , first , last , pay ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
object_1 = Employee('john' , 'smith' , 100)
object_2 = Employee('Pablo' , 'Escobar' , 200)
object_1.fullname()
print(Employee.fullname(object_1))