from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.config import PREFIX, HOST, PORT, SSL_ENABLE, SSL_KEY_PATH, SSL_CERT_PATH
from routers import getAnswer

app = FastAPI(
    title="ChatGPT Answer API",
    description="An API to get answers using OpenAI",
    version="1.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(getAnswer.router, prefix=PREFIX, tags=["Answer"])

if __name__ == '__main__':
    if SSL_ENABLE:
        uvicorn.run(app, host=HOST, port=PORT, ssl_certfile=SSL_CERT_PATH, ssl_keyfile=SSL_KEY_PATH)
    else:
        uvicorn.run(app, host=HOST, port=PORT)