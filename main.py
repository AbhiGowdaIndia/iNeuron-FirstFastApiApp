# importing libraries
import uvicorn
from fastapi import FastAPI

# creating the App object
app = FastAPI()

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {"message":"Hello world!"}

# run the app with uvicorn
# will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=5049)

# command to run the app
# uvicorn main:app --reload