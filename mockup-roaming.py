from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import Optional

app = FastAPI()

class RequestData(BaseModel):
    msisdn: Optional[str] = None
    imsi: str
    mccmnc: str

class ResponseData(BaseModel):
    error_code: int
    error_description: str

@app.post("/api/mockup")
async def mockup_api(request_data: RequestData):
    # Log the received data
    print("Received data:")
    print(request_data)
    # Perform some processing based on the received data
    # ...
    # Prepare the response data
    response_data = ResponseData(error_code=0, error_description="Success")
    # Log the response data
    print("Response data:")
    print(response_data)
    return response_data
