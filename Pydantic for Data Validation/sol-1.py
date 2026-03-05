from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import Dict

class Student(BaseModel):
    name: str = Field(min_length=5,max_length=50, description="Provide the name of the student")
    email: EmailStr = Field(description="Provide a valid email of the student", examples=['abc@gmail.com'])
    age: int = Field(gt=0, le=18)

    # This field validator is used to validate if email belongs to masai.com or not. 
    #called automatically,
    # @=antation, email_validator function require cls=class varible(name,email,age) can use
    #email user can provide value, return class parameter, 
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # abc@masai.com
        #value.split('@')=['abc', 'masai.com'] , 0=abc,1=masai.com;-1=masai.com
        #domain_name=masai.com
        domain_name = value.split('@')[-1]  # ['abc', 'masai.com'] 

        if domain_name != 'masai.com':
            raise ValueError('Not a valid domain for email.')

        return value


 # default value of mode is `after`.
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if value < 0 and value > 19:
            raise ValueError("Invalid age provided.")
        
        return value

student_info = {'name' : 'Chandrasekhar', 'email' : 'abc@masai.com', 'age' : 14}
student = Student(**student_info)
print("name=",student.name)
print("email=",student.email)
print("age=",student.age)
