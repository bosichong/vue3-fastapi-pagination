'''
Author: J.sky bosichong@qq.com
Date: 2022-11-17 09:45:51
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2023-02-13 17:37:01
FilePath: /vue3-fastapi/fastapi-backend/main.py
'''
import os,sys
from faker import Faker
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import Union
from fastapi.middleware.cors import CORSMiddleware  # 解决跨域
import uvicorn as uvicorn
from sqlalchemy.orm import Session
from database import Base,engine,get_db
from models import Item
from crud import create_item,get_item_count,get_items

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

__version__ = "0.0.1"
description = """
vue3-fastapi-test 数据分页,文件上传的一些测试. 🚀
"""



app = FastAPI(
    title="vue3-fastapi-test",
    description=description,
    version=__version__,
    terms_of_service="#",
    license_info={
        "name": "Apache 2.0",
        "url":  "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# 配置允许域名
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",

]

# 配置允许域名列表、允许方法、请求头、cookie等
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine) # create all tables
# 创建测试数据
item_count = 999
fk = Faker(locale="zh-CN")
db = get_db()
k = get_item_count(db)
if (get_item_count(db)==0):
    for i in range(item_count):
        addr = fk.address()
        item = Item(addr=addr)
        create_item(db,item)



@app.get("/")
def test():
    return "vue3-fastapi-test"




@app.get("/getitems")
def get_item_list(skip: int = 0, limit: int = 10,db:Session = Depends(get_db)):
    print(skip,limit)
    data = dict()
    data["items"] = get_items(db=db,skip=skip,limit=limit)
    data["item_count"] = get_item_count(db)
    return data


if __name__ == '__main__':
    print('少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了')
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, )
    