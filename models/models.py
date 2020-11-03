from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class Student(Base):
    __tablename__ = 't_student'
    s_id = Column(Integer, primary_key=True)
    s_name = Column(String(128), unique=False)
    s_email = Column(String(128), unique=False)
    s_area = Column(String(128), unique=False)
    s_univ = Column(String(128), unique=False)
    s_big_tag = Column(Text)
    s_mid_tag = Column(Text)
    s_sml_tag_1 = Column(Text)
    s_sml_tag_2 = Column(Text)
    s_hashed_password = Column(String(128))

    def __init__(self, s_name=None, s_email=None, s_area=None, s_univ=None, s_big_tag=None, s_mid_tag=None, s_sml_tag_1=None, s_sml_tag_2=None, s_hashed_password=None):
        self.s_name = s_name
        self.s_email = s_email
        self.s_area = s_area
        self.s_univ = s_univ
        self.s_big_tag = s_big_tag
        self.s_ = s_mid_tag
        self.s_sml_tag_1 = s_sml_tag_1
        self.s_sml_tag_2 = s_sml_tag_2
        self.s_hashed_password = s_hashed_password

    def __repr__(self):
        return '<Title %r>' % (self.name)

#以下を追加
class Circle(Base):
    __tablename__ = 't_circle'
    c_id = Column(Integer, primary_key=True)
    c_name = Column(String(128), unique=False)
    c_area = Column(String(128), unique=False)
    c_univ = Column(String(128), unique=False)
    c_big_tag = Column(Text)
    c_mid_tag = Column(Text)
    c_sml_tag_1 = Column(Text)
    c_sml_tag_2 = Column(Text)
    c_desc = Column(Text)
    c_image = Column(Text)
    c_hashed_password = Column(String(128))

    def __init__(self, c_name=None, c_area=None, c_univ=None, c_big_tag=None, c_mid_tag=None, c_sml_tag_1=None, c_sml_tag_2=None, c_desc=None, c_image=None, c_hashed_password=None):
        self.c_name = c_name
        self.c_area = c_area
        self.c_univ = c_univ
        self.c_big_tag = c_big_tag
        self.c_mid_tag = c_mid_tag
        self.c_sml_tag_1 = c_sml_tag_1
        self.c_sml_tag_2 = c_sml_tag_2
        self.c_desc = c_desc
        self.c_image = c_image
        self.c_hashed_password = c_hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.c_name)
#追加終わり


class Favorite(Base):
    __tablename__ = 't_favorite'
    id = Column(Integer, primary_key=True)
    s_id = Column(Integer)
    c_id = Column(Integer)

    def __init__(self, s_id=None, c_id=None):
        self.s_id = s_id
        self.c_id = c_id

    # def __repr__(self):
    #     return '<Name %r>' % (self.name)



class Message(Base):
    __tablename__ = 't_message'
    id = Column(Integer, primary_key=True)
    s_id = Column(Integer)
    c_id = Column(Integer)
    message = Column(Text)
    #date = Column(DateTime, default=datetime.now())        //あとで追加

    def __init__(self, s_id=None, c_id=None, message=None):
        self.s_id = s_id
        self.c_id = c_id
        self.message = message
        #self.date= date                                    //あとで追加

    # def __repr__(self):
    #     return '<Name %r>' % (self.name)
