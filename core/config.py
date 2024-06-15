import httpx
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY")
PROXY = os.getenv("PROXY")
PREFIX = os.getenv("PREFIX", "/api/v1")
HOST = os.getenv("API_HOST", "0.0.0.0")
PORT = int(os.getenv("API_PORT", 8000))

SSL_ENABLE = os.getenv("SSL_ENABLE", "false").lower() == "true"
SSL_KEY_PATH = os.getenv("SSL_KEY_PATH", "key.pem")
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH", "cert.pem")


client = OpenAI(
    api_key=API_KEY,
    http_client=httpx.Client(proxy=PROXY)
)
