from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routs.Journal_routs import iRef_Data1_api_router

origins = [
    "http://localhost:4200"
          ]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600
)
app.include_router(iRef_Data1_api_router)
