from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str]= None):
    # http://127.0.0.1:8000/blog?limit=50&published=true
    if published:
        return {'data': f'Only {limit} PUBLISHED blogs can be showed'}
    else:
        return {'data': f'Only {limit} blogs can be showed'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'Unpublished Posts' }

@app.get('/blog/{id}')
def show_blog(id:int):
    return {'data': id }

@app.get('/blog/{id}/comments')
def show_blog_comments(id:int):
    return {'data': 'Some Blog comments'}

# Create a Pydantic class for Blog posts 
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# Create a post with the post method
@app.post('/blog')
def create_blog_post(blog: Blog):
    return {'data': f'This is the Title {blog.title}'}
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5073)