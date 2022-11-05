import logging
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import json
import numpy
import pandas as pd
import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD","docker")
REDIS_PORT = os.getenv("REDIS_PORT","6379")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

log = logging.getLogger(__name__)


app = FastAPI(title="NBA API")
app.mount("/css", StaticFiles(directory="./css"))
app.mount("/templates", StaticFiles(directory="./templates"))

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):

    json_data = r.get("dashboard_data")
    data = json.loads(json_data)
    df = pd.DataFrame(data)
    titles = df.columns.values.tolist()

    return templates.TemplateResponse(
        "index.html", {"request": request, "data": df.to_html()}
    )