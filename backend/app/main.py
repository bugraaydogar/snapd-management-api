from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .snapd import SnapdClient

class Snap(BaseModel):
    name: str


class SideLoadReq(BaseModel):
    snap: str
    path: str


app = FastAPI()
snap_client = SnapdClient()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/system-info")
def system_info():
    response = snap_client.snap_system_info()
    return response


@app.post("/sideload")
def sideLoad(sideload: SideLoadReq):
    response = snap_client.side_load_snap(sideload.snap, sideload.path)
    return response


@app.post("/refresh")
def refresh():
    response = snap_client.refresh()
    return response


@app.post("/revert")
def revert(snap: Snap):
    print(snap.name)
    response = snap_client.revert(snap.name)
    return response

