'''
Author: J.sky bosichong@qq.com
Date: 2022-11-17 10:04:37
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-17 11:48:44
FilePath: /vue3-fastapi/fastapi-backend/crud.py
'''
from sqlalchemy.orm import Session
from models import Item


def create_item(db: Session, item: Item):
    db_item = Item(addr=item.addr)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

def get_item_count(db: Session):
    return db.query(Item).count()
# offset: 表示要跳过多少条数据,limit: 表示取几条数据,
def get_items(db: Session,skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()