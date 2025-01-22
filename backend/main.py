from fastapi import FastAPI
from routers import router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
