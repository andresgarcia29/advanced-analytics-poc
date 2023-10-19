from fastapi import FastAPI

import log
from core import HealthCheck
from router import router

app = FastAPI()

logger = log.setup_custom_logger("app")


@app.get("/healthz")
def healthz():
    return HealthCheck(message="I'm alivie")


app.include_router(router=router)
