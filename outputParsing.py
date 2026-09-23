from pydantic import BaseModel 

class Student(BaseModel):
      name :str
      age : int | None = None
      course : str = Field()

st = Student(name = "anay", age = 35 , course = "Java")

print(st)