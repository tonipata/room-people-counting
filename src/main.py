from fastapi import FastAPI
import start_service as start_service
from log import get_log
import os
import pandas as pd
from contextlib import asynccontextmanager

log = get_log(__name__)

app = FastAPI()

app.include_router(start_service.router)

log.info("Starting application")
