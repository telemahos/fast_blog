from typing import Optional
from pydantic import BaseModel
from typing import List


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

class BlogBase(BaseModel):
    title: str
    body: str
    # author_id: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    # Refers to the first class Blog
    the_blogs: List[Blog] = []      
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    owner: ShowUser
    class Config():
        orm_mode = True

class login(BaseModel):
    username: str
    password: str