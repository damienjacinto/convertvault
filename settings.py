import os

DEBUG = bool(os.getenv("DEBUG", False))
RELOAD = bool(os.getenv("RELOAD", False))
PORT = int(os.getenv("PORT", 8080))