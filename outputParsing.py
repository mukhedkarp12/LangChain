from pydantic import BaseModel 

class Student(BaseModel):
      name :str
      age : int
      course : str
st = Student(name = "Pratibha", age = 35 , course = "Java")
print(st)