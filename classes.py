class Hriday:
    x=5

id=Hriday()
print(id.x)

class StudentDetails:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age

p1=StudentDetails("Hriday",99,20)
print(p1.name,p1.age,p1.marks)
