from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from mod.api import stat
from mod.post import *
from mod.model import Body
import uvicorn
import os
import random
import sqlalchemy

app = FastAPI()
from mod.db import global_init
global_init("database.db")

def verify_token(req: Request):
    key = req.headers["Authorization"].split(':')

    if not DB._check_token(key[0], key[1]):
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return key[0]

@app.get('/')
async def main_page():
    return {'sorry': 'main page in dev'}

@app.post('/status')
async def status_page(req: Request, authorized: bool = Depends(verify_token)):
    if authorized:
        return {'stats': stat()}

@app.post("/api/")
async def api_req(req: Request, data: Body, authorized: bool = Depends(verify_token)):
    if authorized:
        return DB._add_data(authorized, data)

@app.post("/data/")
async def get_data(req: Request, authorized: bool = Depends(verify_token)):
    if authorized:
        return DB._get_metrika(authorized)

if __name__ == "__main__":
    uvicorn.run('app:app',
        host="0.0.0.0", 
        port=int(os.environ.get("PORT", 5000)),
        log_level="debug",
        http="h11",
        reload=True, 
        use_colors=True,
        workers=3
    )