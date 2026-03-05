from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Optional

# 1. Address Model
class Address(BaseModel):
    # City must be a string with a minimum length of 3
    city: str = Field(description="Provide the city name", min_length=3)
    # Pincode must be a string exactly 6 digits long
    pincode: str = Field(description="Provide the pincode", pattern=r"^\d{6}$")

# 2. User Model
class User(BaseModel):
    user_id: int = Field(description="Provide the unique user ID")
    name: str = Field(description="Provide the name of the user")
    # Validates email format
    email: EmailStr = Field(description="Provide a valid email address")
    # Age must be greater than or equal to 18
    age: int = Field(description="Provide the age of the user", ge=18)
    # Nested Address model
    address: Address
    # Optional boolean with default False
    is_premium: Optional[bool] = False

# --- Example Usage ---
try:
    user_data = {
        "user_id": 101,
        "name": "chandrasekhar",
        "email": "john@example.com",
        "age": 25,
        "address": {
            "city": "Mumbai",
            "pincode": "400001"
        },
        "is_premium": True
    }
    user = User(**user_data)
    print(user.model_dump_json(indent=6))
except ValidationError as e:
    print(e.json())
