from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_items(name: Optional[str] = None, age: Optional[int] = None):
    """
    Accepts optional 'name' (string) and 'age' (integer) query parameters
    and returns them as a JSON response.
    """
    return {
        "name": "chandrasekhar",
        "age": "26"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)

    
