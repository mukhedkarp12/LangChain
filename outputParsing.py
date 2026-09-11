from pydantic import BaseModel 

class Student(BaseModel):
      name :str
      age : int
      course : str
st = Student(name = "anay", age = 35 , course = "Java")
print(st)