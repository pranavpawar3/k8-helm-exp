import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from typing import Optional, List

app = FastAPI()

@app.get("/initiate", response_description="starts the service")
async def init():
    print("Microservice is successfully triggered")
    return "Microservice is successfully triggered"