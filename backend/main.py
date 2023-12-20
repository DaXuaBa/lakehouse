from fastapi import FastAPI
from backend.db import model
from backend.db.database import engine
from backend.router import user, webhook
from backend.utils import authentication
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

list_router = [
    user.router,
    authentication.router,
    webhook.router
]

@app.get("/")
async def index():
    return "Một bông hoa đẹp, không nên thuộc về một kẻ chỉ biết ngắm chứ không biết chăm"

for router in list_router: 
    app.include_router(router,prefix="/run_be") 

model.Base.metadata.create_all(bind=engine)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
