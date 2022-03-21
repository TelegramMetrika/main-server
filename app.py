from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from mod.api import stat
from mod.post import *
from mod.model import Body, Reg
from mod.utils import message, status
from mod.error import errors
import datetime
import uvicorn
import os

app = FastAPI()
server_time = datetime.datetime.now()
from mod.db import global_init
global_init("database.db")

def verify_token(req: Request):
    try:
        key = req.headers["Authorization"].split(':')
    except:
        raise HTTPException(
            status_code=401,
            detail='Токен инвалид -_-, надо id:key'
        )

    if not DB._check_token(key[0], key[1]):
        raise HTTPException(
            status_code=401,
            detail=errors[401]
        )
    return key[0]

@app.get('/')
async def main_page():
    return message('Главная страница в разработке')

@app.post('/status')
async def status_page(req: Request):
    """Запрос состояния сервера"""
    return {'stats': stat(server_time)}

@app.post("/create/")
async def api_req_create(req: Request, data: Reg):
    """Добавить данные в бд"""
    try:
        return status(DB._create_metrika(data))
    except:
        raise HTTPException(status_code=500, detail="Ошибка сервера, проверьте отправляемые данные!")

@app.post("/add/")
async def api_req_add(req: Request, data: Body, authorized: bool = Depends(verify_token)):
    """Добавить данные в бд"""
    if authorized:
        try:
            return {"status_code": 200, "result": DB._add_data(authorized, data)}
        except:
            raise HTTPException(status_code=500, detail="Ошибка сервера, проверьте отправляемые данные!")

@app.post("/get/")
async def get_data(req: Request, authorized: bool = Depends(verify_token)):
    """Достать данные из бд"""
    if authorized:
        try:
            return DB._get_metrika(authorized)
        except:
            raise HTTPException(status_code=500, detail="Ошибка сервера, проверьте отправляемые данные!")

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