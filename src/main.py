from fastapi import FastAPI
from routes import base
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()
app.include_router(base.base_router)
