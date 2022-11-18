'''
Author: J.sky bosichong@qq.com
Date: 2022-11-17 09:57:40
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-17 10:35:52
FilePath: /vue3-fastapi/fastapi-backend/model.py
'''

from database import Base
from sqlalchemy import String,Column,Integer

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer,primary_key=True,autoincrement=True)
    addr = Column(String(256), nullable=False,index=True)