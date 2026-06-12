from fastapi import FastAPI
from app.routers import auth, links, redirect

app = FastAPI()

app.include_router(auth.router)
app.include_router(links.router)
app.include_router(redirect.router)