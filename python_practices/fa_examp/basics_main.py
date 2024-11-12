from fastapi import FastAPI, Depends
import time
from starlette.middleware.base import BaseHTTPMiddleware

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Custom Value Added from Middleware"
        return response

#Example: Background Tasks
from fastapi import BackgroundTasks
def write_log(message: str):
    # FastAPI allows you to run background tasks for operations 
    # that don't need to block the main request/response cycle.
    with open("log.txt", "a") as f:
        f.write(message)

app = FastAPI()
app.add_middleware(CustomMiddleware)

################## The Get API Example
@app.get("/")
def read_root(background_tasks:BackgroundTasks):
    background_tasks.add_task(write_log, "Root API Hit")
    # localhost:8000
    return {"message": "Logged with Root API Hit Message in background task, also can not middle ware added header"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # http://localhost:8000/items/42?q=test
    return {"item_id": item_id, "q": q}

@app.get("/items/")
def get_items(q: str = None, limit: int = 10):
    # {"q":null,"limit":10} # /items => {"q":null,"limit":10}
    # http://localhost:8000/items/?q=example&limit=5 => {"q":"example","limit":5}
    return {"q": q, "limit": limit}

################## The Get API Example POST, PUT, PATCH, and DELETE requests, you usually send data 

from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/itemsp/")
def create_item(item: Item):
    # POST : {"name": "Sample Item","price": 20.5} to items
    return {"item": item}

def get_db():
    db = "Database Connection"
    try: yield db    
    finally: db = None  # Close database connection

@app.get("/itemsDI/{item_id}")
def get_item(item_id: int, db: str = Depends(get_db)):
    return {"item_id": item_id, "db": db, "about":"FastAPI has a powerful dependency injection system. Dependencies can be used to share common logic like database connections, authentication, etc."}


# FastAPI allows you to specify the response model for your endpoints, which helps to validate 
# and document the response structure.
@app.post("/itemsRM/", response_model=Item)
def create_item(item: Item):
    return item

async def get_item_from_db(item_id):
    time.sleep(2)
    #return "Nishu" # {"item_id": 1,"item": "Nishu"}
    return Item(name=1,description="some",price=1.9, tax=1.9); 
    #{"item_id": 1,"item": {"name": "1","description": "some","price": 1.9,"tax": 1.9}}

@app.get("/items_async/{item_id}")
async def read_item(item_id: int):
    item = await get_item_from_db(item_id)  # Imagine an async DB call here
    return {"item_id": item_id, "item": item}

from fastapi import HTTPException

@app.get("/items_exec/{item_id}")
def get_item(item_id: int):
    db={1:"Rec1",2:"Rec2",3:"Rec3",4:"Rec4"}
    if item_id not in db:
        raise HTTPException(status_code=404, detail={"error":"Item not found","concept":"HttpException: Allows you to raise errors with a specific status code and message."})
    return {"item_id": item_id, "name": db[item_id]}

# Upload File
from fastapi import File, UploadFile, HTTPException
# Prequiste : pip install python-multipart
# pip install python-magic
import magic
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/gif"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB limit
# Function to validate file type and size
def validate_file(file: UploadFile):
    # Check file extension
    ext = file.filename.split('.')[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file extension. Allowed extensions: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    # Check MIME type using python-magic
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_buffer(file.file.read(1024))  # Read the first 1KB for magic signature
    file.file.seek(0)  # Reset the file pointer after reading

    if file_mime_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_MIME_TYPES)}"
        )
    # Check file size
    if len(file.file.read()) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds the 5MB limit."
        )
    # V.imp without this size will be 0 every time file passed and read should be set to zero
    file.file.seek(0)  

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    validate_file(file)
    # Also if try validate_file return content and use with await will get following error 
    """
    es\Python312\site-packages\fastapi\routing.py", line 159, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\nishu\workspace\aws\python_practices\fa_examp\basics_main.py", line 130, in upload_file
    content = await validate_file(file)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: object bytes can't be used in 'await' expression
    """
    content = await file.read()
    print(content)
    return {"filename": file.filename, "file_size": len(content)}


########### TODOs FOllowing The Admin pop up working but not available
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user(token: str = Depends(oauth2_scheme)):
    print(1111)
    if token != "valid_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return {"username": "admin"}

@app.get("/users/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

# async def: Defines the function as asynchronous.
# await: Used to wait for asynchronous tasks to complete.
# python -m pip install fastapi 
#python -m uvicorn basics_main:app --reload

""" Some more basics for reference
Example: Test API Endpoint
from fastapi.testclient import TestClient
client = TestClient(app)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

Versioning
You can version your API by adding version numbers to the path.
Example: API Versioning
@app.get("/v1/items/{item_id}")
def get_item_v1(item_id: int):
    return {"item_id": item_id}

@app.get("/v2/items/{item_id}")
def get_item_v2(item_id: int):
    return {"item_id": item_id, "new_feature": "added"}

"""
