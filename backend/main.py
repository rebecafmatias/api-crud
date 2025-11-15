from fastapi import FastAPI
from database import engine
import models  # Ensure models are imported for table creation
from router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)